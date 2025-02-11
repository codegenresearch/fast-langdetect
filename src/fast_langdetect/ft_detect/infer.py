# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午8:30
# @Author  : sudoskys
# @File    : infer.py
# @Software: PyCharm
import logging
import os
from pathlib import Path
from typing import Dict, Union, List

import fasttext
from robust_downloader import download

logger = logging.getLogger(__name__)
MODELS = {"low_mem": None, "high_mem": None}
FTLANG_CACHE = os.getenv("FTLANG_CACHE", "/tmp/fasttext-langdetect")

try:
    # silences warnings as the package does not properly use the python 'warnings' package
    # see https://github.com/facebookresearch/fastText/issues/1056
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass


class DetectError(Exception):
    """Custom exception for detection errors."""
    pass


def get_model_map(low_memory=False):
    """
    Get the model map based on the low_memory flag.

    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :return: Tuple containing mode, cache path, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def get_model_loaded(
        low_memory: bool = False,
        download_proxy: str = None
):
    """
    Load the appropriate model based on the low_memory flag.

    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param download_proxy: Proxy for downloading the model.
    :return: Loaded fastText model.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise Exception(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            download(url=url, folder=cache, filename=name, proxy=download_proxy)
            raise e
        else:
            return loaded_model

    download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
    loaded_model = fasttext.load_model(model_path)
    MODELS[mode] = loaded_model
    return loaded_model


def detect(text: str, *,
           low_memory: bool = True,
           model_download_proxy: str = None
           ) -> Dict[str, Union[str, float]]:
    """
    Detect the language of a given text.

    :param text: The text to detect the language of. It is assumed that the text does not contain newline characters.
    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param model_download_proxy: Proxy for downloading the model.
    :return: Dictionary containing the detected language and its confidence score.
    :raises ValueError: If the input text contains newline characters.
    :raises DetectError: If an error occurs during detection.
    """
    if '\n' in text:
        raise ValueError("Input text should not contain newline characters.")
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {
            "lang": label,
            "score": score,
        }
    except Exception as e:
        raise DetectError(f"Error during detection: {e}")


def detect_multilingual(text: str, *,
                        low_memory: bool = True,
                        model_download_proxy: str = None,
                        k: int = 5,
                        threshold: float = 0.0,
                        on_unicode_error: str = "strict"
                        ) -> List[dict]:
    """
    Detect multiple languages in a given text.

    :param text: The text to detect languages in. It is assumed that the text does not contain newline characters.
    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param model_download_proxy: Proxy for downloading the model.
    :param k: Number of top predictions to return.
    :param threshold: Confidence threshold for predictions.
    :param on_unicode_error: Error handling strategy for Unicode errors.
    :return: List of dictionaries containing detected languages and their confidence scores.
    :raises ValueError: If the input text contains newline characters.
    :raises DetectError: If an error occurs during multilingual detection.
    """
    if '\n' in text:
        raise ValueError("Input text should not contain newline characters.")
    try:
        model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({
                "lang": label,
                "score": score,
            })
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        raise DetectError(f"Error during multilingual detection: {e}")


# Additional test cases for coverage
def test_detect_multilingual_low_memory():
    result = detect_multilingual("hello world", low_memory=True)
    assert any(item["lang"] == "en" for item in result), "Multilingual detection error for English"
    result = detect_multilingual("你好世界", low_memory=True)
    assert any(item["lang"] == "zh" for item in result), "Multilingual detection error for Chinese"
    result = detect_multilingual("こんにちは世界", low_memory=True)
    assert any(item["lang"] == "ja" for item in result), "Multilingual detection error for Japanese"
    result = detect_multilingual("안녕하세요 세계", low_memory=True)
    assert any(item["lang"] == "ko" for item in result), "Multilingual detection error for Korean"
    result = detect_multilingual("Bonjour le monde", low_memory=True)
    assert any(item["lang"] == "fr" for item in result), "Multilingual detection error for French"
    result = detect_multilingual("Hallo Welt", low_memory=True)
    assert any(item["lang"] == "de" for item in result), "Multilingual detection error for German"
    result = detect_multilingual("Hola mundo", low_memory=True)
    assert any(item["lang"] == "es" for item in result), "Multilingual detection error for Spanish"
    result = detect_multilingual("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=True)
    assert any(item["lang"] == "zh" for item in result), "Multilingual detection error for Traditional Chinese"
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    assert any(item["lang"] == "en" for item in result), "Multilingual detection error for English in mixed text"
    assert any(item["lang"] == "zh" for item in result), "Multilingual detection error for Chinese in mixed text"
    assert any(item["lang"] == "ru" for item in result), "Multilingual detection error for Russian in mixed text"

def test_detect_low_memory():
    result = detect("hello world", low_memory=True)
    assert result["lang"] == "en", "Detection error for English"
    result = detect("你好世界", low_memory=True)
    assert result["lang"] == "zh", "Detection error for Chinese"
    result = detect("こんにちは世界", low_memory=True)
    assert result["lang"] == "ja", "Detection error for Japanese"
    result = detect("안녕하세요 세계", low_memory=True)
    assert result["lang"] == "ko", "Detection error for Korean"
    result = detect("Bonjour le monde", low_memory=True)
    assert result["lang"] == "fr", "Detection error for French"
    result = detect("Hallo Welt", low_memory=True)
    assert result["lang"] == "de", "Detection error for German"
    result = detect("Hola mundo", low_memory=True)
    assert result["lang"] == "es", "Detection error for Spanish"
    result = detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=True)
    assert result["lang"] == "zh", "Detection error for Traditional Chinese"

def test_failed_example_low_memory():
    try:
        detect("hello world\nNEW LINE", low_memory=True)
    except ValueError as e:
        assert str(e) == "Input text should not contain newline characters.", "Detection exception error for newline in detect"
    try:
        detect_multilingual("hello world\nNEW LINE", low_memory=True)
    except ValueError as e:
        assert str(e) == "Input text should not contain newline characters.", "Detection exception error for newline in detect_multilingual"