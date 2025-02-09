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

# Silences warnings as the package does not properly use the python 'warnings' package
# see https://github.com/facebookresearch/fastText/issues/1056
fasttext.FastText.eprint = lambda *args, **kwargs: None


class DetectError(Exception):
    """Custom exception for language detection errors."""
    pass


def get_model_map(low_memory=False):
    """
    Get the model map based on the low memory flag.

    :param low_memory: Whether to use low memory mode.
    :return: A tuple containing the mode, cache path, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def get_model_loaded(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText._FastText:
    """
    Load the appropriate FastText model.

    :param low_memory: Whether to use low memory mode.
    :param download_proxy: Proxy server for downloading the model.
    :return: The loaded FastText model.
    :raises DetectError: If there is an error loading or downloading the model.
    """
    mode, cache, name, url = get_model_map(low_memory)
    loaded = MODELS.get(mode, None)
    if loaded:
        return loaded
    model_path = os.path.join(cache, name)
    if Path(model_path).exists():
        if Path(model_path).is_dir():
            raise DetectError(f"{model_path} is a directory")
        try:
            loaded_model = fasttext.load_model(model_path)
            MODELS[mode] = loaded_model
            return loaded_model
        except Exception as e:
            logger.error(f"Error loading model {model_path}: {e}")
            raise DetectError(f"Error loading model {model_path}: {e}")

    try:
        download(url=url, folder=cache, filename=name, proxy=download_proxy, retry_max=3, timeout=20)
        loaded_model = fasttext.load_model(model_path)
        MODELS[mode] = loaded_model
        return loaded_model
    except Exception as e:
        logger.error(f"Error downloading or loading model {model_path}: {e}")
        raise DetectError(f"Error downloading or loading model {model_path}: {e}")


def detect(text: str, *, low_memory: bool = True, model_download_proxy: str = None) -> Dict[str, Union[str, float]]:
    """
    Detect the language of a given text.

    :param text: The text to detect the language of.
    :param low_memory: Whether to use low memory mode.
    :param model_download_proxy: Proxy server for downloading the model.
    :return: A dictionary with the detected language and its confidence score.
    :raises DetectError: If there is an error during language detection.
    """
    model = get_model_loaded(low_memory=low_memory, download_proxy=model_download_proxy)
    labels, scores = model.predict(text)
    label = labels[0].replace("__label__", '')
    score = min(float(scores[0]), 1.0)
    return {
        "lang": label,
        "score": score,
    }


def detect_multilingual(text: str, *, low_memory: bool = True, model_download_proxy: str = None, k: int = 5,
                        threshold: float = 0.0, on_unicode_error: str = "strict") -> List[dict]:
    """
    Detect multiple languages in a given text.

    :param text: The text to detect languages in.
    :param low_memory: Whether to use low memory mode.
    :param model_download_proxy: Proxy server for downloading the model.
    :param k: Number of top predictions to return.
    :param threshold: Score threshold for predictions.
    :param on_unicode_error: How to handle Unicode errors during prediction.
    :return: A list of dictionaries with detected languages and their confidence scores.
    :raises DetectError: If there is an error during multilingual language detection.
    """
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


# Demonstrating multilingual detection with diverse examples
if __name__ == "__main__":
    examples = [
        "hello world",
        "你好世界",
        "こんにちは世界",
        "안녕하세요 세계",
        "Bonjour le monde",
        "Hallo Welt",
        "Hola mundo",
        "これらの機関主催のコースは、主に基本的なコンピュータの使用を教えることが多いです。例えば、文書処理、中国語入力、インターネットアプリケーションなどです。",
        "Hello, world!你好世界!Привет, мир!"
    ]

    for example in examples:
        try:
            print(f"Text: {example}")
            print("Multilingual Detection:", detect_multilingual(example, low_memory=False))
        except DetectError as e:
            print(e)