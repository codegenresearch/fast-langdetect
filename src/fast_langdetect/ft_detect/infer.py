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


def get_model_map(low_memory=False) -> tuple:
    """
    Get the model map based on the low_memory flag.

    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :return: A tuple containing the mode, cache path, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def get_model_loaded(
        low_memory: bool = False,
        download_proxy: str = None
) -> fasttext.FastText._FastText:
    """
    Load the appropriate model based on the low_memory flag.

    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param download_proxy: Proxy URL for downloading the model.
    :return: The loaded fastText model.
    :raises Exception: If there is an error loading or downloading the model.
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
    Detect the language of the given text.

    Assumes the input text is a non-empty string.

    :param text: The text to detect the language of.
    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param model_download_proxy: Proxy URL for downloading the model.
    :return: A dictionary containing the detected language and its confidence score.
             Example: {"lang": "en", "score": 0.99}
    :raises DetectError: If there is an error during language detection.
    """
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
        raise DetectError(f"Failed to detect language: {e}")


def detect_multilingual(text: str, *,
                        low_memory: bool = True,
                        model_download_proxy: str = None,
                        k: int = 5,
                        threshold: float = 0.0,
                        on_unicode_error: str = "strict"
                        ) -> List[dict]:
    """
    Detect multiple languages in the given text.

    Assumes the input text is a non-empty string.

    :param text: The text to detect languages in.
    :param low_memory: Boolean flag to determine whether to use the low memory model.
    :param model_download_proxy: Proxy URL for downloading the model.
    :param k: Number of top predictions to return.
    :param threshold: Confidence score threshold for predictions.
    :param on_unicode_error: Error handling strategy for Unicode errors.
    :return: A list of dictionaries, each containing a detected language and its confidence score.
             Example: [{"lang": "en", "score": 0.99}, {"lang": "fr", "score": 0.01}]
    :raises DetectError: If there is an error during language detection.
    """
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
        raise DetectError(f"Failed to detect multiple languages: {e}")