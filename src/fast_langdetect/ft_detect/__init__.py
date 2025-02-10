# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
import logging
from fast_langdetect.ft_detect import detect, detect_multilingual  # noqa: F401

# Setting up logging
logging.basicConfig(level=logging.INFO)

def is_japanese(string):
    """
    Check if the string contains Japanese characters.
    :param string: The string to check.
    :return: True if Japanese characters are found, False otherwise.
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False

def detect_language(sentence, *, low_memory: bool = True):
    """
    Detect the language of the given sentence.
    :param sentence: The sentence to detect the language of.
    :param low_memory: Whether to use low memory mode.
    :return: Language code as a two uppercase letters string (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).
    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code

def detect_langs(sentence, *, low_memory: bool = True):
    """
    Detect language with a deprecated warning.
    :param sentence: The sentence to detect the language of.
    :param low_memory: Whether to use low memory mode.
    :return: Language code as a two uppercase letters string (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).
    """
    logging.warning("The function `detect_langs` is deprecated. Use `detect_language` instead.")
    return detect_language(sentence, low_memory=low_memory)