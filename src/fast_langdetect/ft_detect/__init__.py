# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect
from .infer import detect_multilingual  # noqa: F401
import logging

# Setting up logging for deprecation warnings
logger = logging.getLogger(__name__)


def is_japanese(string):
    """
    Check if the string contains Japanese characters.
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect language and return the language code in uppercase.

    :param sentence: str - The sentence to detect the language of.
    :param low_memory: bool - Whether to use low memory mode (default: True).
    :return: str - The detected language code in uppercase.
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def detect_langs(sentence, *, low_memory: bool = True):
    """
    Detect language and return the language code in uppercase.

    :param sentence: str - The sentence to detect the language of.
    :param low_memory: bool - Whether to use low memory mode (default: True).
    :return: str - The detected language code in uppercase.
    """
    logger.warning("The function detect_langs is deprecated. Use detect_language instead.")
    return detect_language(sentence, low_memory=low_memory)