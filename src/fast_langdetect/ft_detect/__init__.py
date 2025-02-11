# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

import logging
from .infer import detect
from .infer import detect_multilingual  # noqa: F401

# Setting up logging
logging.basicConfig(level=logging.WARNING)


def is_japanese(string):
    """
    Check if the string contains Japanese characters.

    :param string: str - The string to check.
    :return: bool - True if the string contains Japanese characters, False otherwise.
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect language.

    :param sentence: str - The sentence to detect the language of.
    :param low_memory: bool - Whether to use low memory mode (default: True).
    :return: str - Language code in uppercase (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def detect_langs(sentence, *, low_memory: bool = True):
    """
    Detect language.
    This function is deprecated. Use `detect_language` instead.

    :param sentence: str - The sentence to detect the language of.
    :param low_memory: bool - Whether to use low memory mode (default: True).
    :return: str - Language code in uppercase (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).
    """
    logging.warning("The `detect_langs` function is deprecated. Use `detect_language` instead.")
    return detect_language(sentence, low_memory=low_memory)