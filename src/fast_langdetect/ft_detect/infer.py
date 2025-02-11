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
    # Suppress warnings from fastText
    fasttext.FastText.eprint = lambda *args, **kwargs: None
except Exception:
    pass


class DetectError(Exception):
    """Custom exception for detection errors."""
    pass


def get_model_map(low_memory=False) -> tuple:
    """
    Get model map based on low_memory flag.

    :param low_memory: Use low memory model if True.
    :return: Tuple of mode, cache path, model name, and model URL.
    """
    if low_memory:
        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"
    else:
        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"


def load_model(low_memory: bool = False, download_proxy: str = None) -> fasttext.FastText._FastText:
    """
    Load the appropriate model based on low_memory flag.

    :param low_memory: Use low memory model if True.
    :param download_proxy: Proxy URL for downloading the model.
    :return: Loaded fastText model.
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

    Assumes the input text is a single line.

    :param text: Text to detect the language of.
    :param low_memory: Use low memory model if True.
    :param model_download_proxy: Proxy URL for downloading the model.
    :return: Dictionary with detected language and score.
    :raises DetectError: If there is an error during language detection.
    :raises ValueError: If the input text contains multiple lines.
    """
    if "\n" in text:
        raise ValueError("Input text must be a single line.")
    try:
        model = load_model(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text)
        label = labels[0].replace("__label__", '')
        score = min(float(scores[0]), 1.0)
        return {"lang": label, "score": score}
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

    :param text: Text to detect languages in.
    :param low_memory: Use low memory model if True.
    :param model_download_proxy: Proxy URL for downloading the model.
    :param k: Number of top predictions to return.
    :param threshold: Confidence score threshold for predictions.
    :param on_unicode_error: Error handling strategy for Unicode errors.
    :return: List of dictionaries with detected languages and scores.
    :raises DetectError: If there is an error during language detection.
    """
    try:
        model = load_model(low_memory=low_memory, download_proxy=model_download_proxy)
        labels, scores = model.predict(text=text, k=k, threshold=threshold, on_unicode_error=on_unicode_error)
        detect_result = []
        for label, score in zip(labels, scores):
            label = label.replace("__label__", '')
            score = min(float(score), 1.0)
            detect_result.append({"lang": label, "score": score})
        return sorted(detect_result, key=lambda i: i['score'], reverse=True)
    except Exception as e:
        raise DetectError(f"Failed to detect multiple languages: {e}")