# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect as detect_language
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    """
    Check if the string contains Japanese characters.
    :param string: The string to check.
    :return: True if Japanese characters are found, False otherwise.
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """
    Detect the language of the given sentence and return the language code.
    :param sentence: The sentence to detect the language of.
    :param low_memory: Whether to use low memory mode.
    :return: Language code as a two uppercase letters string (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).
    """
    detected_lang = detect_language(sentence, low_memory=low_memory).get("lang").upper()
    if detected_lang == "JA" and not contains_japanese_characters(sentence):
        detected_lang = "ZH"
    return detected_lang