# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

import logging
from .infer import detect, detect_multilingual  # noqa: F401

# Setting up logging for deprecation warnings
logger = logging.getLogger(__name__)


def is_japanese(string):
    """
    Check if the string contains Japanese characters.

    :param string: str
    :return: bool
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect language.

    :param sentence: str
    :param low_memory: bool
    :return: str
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def detect_langs(sentence, *, low_memory: bool = True):
    """
    Detect language.
    Note: This function is deprecated. Use detect_language instead.

    :param sentence: str
    :param low_memory: bool
    :return: str
    """
    logger.warning("Function detect_langs is deprecated. Use detect_language instead.")
    return detect_language(sentence, low_memory=low_memory)