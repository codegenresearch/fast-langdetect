# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect as detect_language
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    """
    Check if the string contains Japanese characters.
    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """
    Detect language and return the language code in uppercase.
    :param sentence: str sentence
    :param low_memory: bool (default: True) whether to use low memory mode
    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)
    """
    detected_lang = detect_language(sentence, low_memory=low_memory).get("lang").upper()
    if detected_lang == "JA" and not contains_japanese_characters(sentence):
        detected_lang = "ZH"
    return detected_lang