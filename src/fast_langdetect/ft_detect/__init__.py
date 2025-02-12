# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect as detect_language
from .infer import detect_multilingual  # noqa: F401

def contains_japanese_characters(string):
    """\n    Check if the string contains Japanese characters\n    :param string: str\n    :return: bool\n    """
    for ch in string:
        if 0x3040 <= ord(ch) <= 0x30FF or 0x4E00 <= ord(ch) <= 0x9FFF:
            return True
    return False

def identify_language(sentence, *, low_memory: bool = True):
    """\n    Detect language of the given sentence\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    detection_result = detect_language(sentence, low_memory=low_memory)
    lang_code = detection_result.get("lang").upper()
    if lang_code == "JA" and not contains_japanese_characters(sentence):
        lang_code = "ZH"
    return lang_code