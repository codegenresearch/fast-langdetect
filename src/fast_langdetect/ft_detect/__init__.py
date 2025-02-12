# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect as detect_language
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    """\n    Check if the string contains Japanese characters.\n    :param string: The string to check.\n    :return: True if Japanese characters are found, False otherwise.\n    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """\n    Detect the language of the given sentence and return the language code.\n    :param sentence: The sentence to analyze.\n    :param low_memory: Whether to use low memory mode.\n    :return: Language code as a two uppercase letters (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).\n    """
    detected_language = detect_language(sentence, low_memory=low_memory).get("lang").upper()
    if detected_language == "JA" and not contains_japanese_characters(sentence):
        detected_language = "ZH"
    return detected_language