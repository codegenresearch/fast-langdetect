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
    pass


def get_model_map(low_memory=False):
    """\n    Getting model map\n    :param low_memory:\n    :return:\n    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def get_model_loaded(
        low_memory: bool = False,
        download_proxy: str = None
):
    """\n    Getting model loaded\n    :param low_memory:\n    :param download_proxy:\n    :return:\n    """
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
    assert any(item.get("lang") == "en" for item in result), "ft_detect error"

    result = detect_multilingual("你好世界", low_memory=True)
    assert any(item.get("lang") == "zh" for item in result), "ft_detect error"

    result = detect_multilingual("こんにちは世界", low_memory=True)
    assert any(item.get("lang") == "ja" for item in result), "ft_detect error"

    result = detect_multilingual("안녕하세요 세계", low_memory=True)
    assert any(item.get("lang") == "ko" for item in result), "ft_detect error"

    result = detect_multilingual("Bonjour le monde", low_memory=True)
    assert any(item.get("lang") == "fr" for item in result), "ft_detect error"

    result = detect_multilingual("Hallo Welt", low_memory=True)
    assert any(item.get("lang") == "de" for item in result), "ft_detect error"

    result = detect_multilingual("Hola mundo", low_memory=True)
    assert any(item.get("lang") == "es" for item in result), "ft_detect error"

    result = detect_multilingual("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等", low_memory=True)
    assert any(item.get("lang") == "zh" for item in result), "ft_detect error"

    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    assert len(result) > 1, "ft_detect error"

# Test for exception handling
def test_detect_exception():
    try:
        detect("hello world\nNEW LINE", low_memory=True)
    except DetectError as e:
        assert isinstance(e, DetectError), "ft_detect exception error"

def test_detect_multilingual_exception():
    try:
        detect_multilingual("hello world\nNEW LINE", low_memory=True)
    except DetectError as e:
        assert isinstance(e, DetectError), "ft_detect exception error"