# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """\n    Detect language code\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    detected_language = detect(sentence, low_memory=low_memory).get("lang").upper()
    if detected_language == "JA" and not contains_japanese_characters(sentence):
        detected_language = "ZH"
    return detected_language