# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

from .infer import detect as detect_language
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    """\n    Check if the string contains Japanese characters.\n    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """\n    Detect the language of the given sentence and return the language code.\n    \n    :param sentence: The sentence to detect the language of.\n    :param low_memory: Whether to use low memory mode.\n    :return: Language code in uppercase (e.g., ZH, EN, JA, KO, FR, DE, ES, ...).\n    """
    detected_lang = detect_language(sentence, low_memory=low_memory).get("lang").upper()
    if detected_lang == "JA" and not contains_japanese_characters(sentence):
        detected_lang = "ZH"
    return detected_lang