# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

import logging
from .infer import detect
from .infer import detect_multilingual  # noqa: F401
from .ft_detect import detect_language  # Ensure this function is correctly imported

# Setting up logging
logging.basicConfig(level=logging.WARNING)

def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect language
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def detect_langs(sentence, *, low_memory: bool = True):
    """
    Detect language (deprecated)
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)
    """
    logging.warning("The function `detect_langs` is deprecated. Use `detect_language` instead.")
    return detect_language(sentence, low_memory=low_memory)