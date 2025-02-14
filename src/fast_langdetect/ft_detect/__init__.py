# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py

from .infer import detect
from .infer import detect_multilingual  # noqa: F401


def is_japanese(string):
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language(sentence, *, low_memory: bool = True):
    """\n    Detect language\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    result = detect(sentence, low_memory=low_memory)
    lang_code = result.get("lang").upper()
    if lang_code == "JA" and not is_japanese(sentence):
        lang_code = "ZH"
    return lang_code


def comprehensive_detect(sentence, *, low_memory: bool = True):
    """\n    Comprehensive language detection\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: dict with lang and score\n    """
    return detect(sentence, low_memory=low_memory)


def comprehensive_detect_multilingual(sentence, *, low_memory: bool = True):
    """\n    Comprehensive multilingual language detection\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: list of dicts with lang and score\n    """
    return detect_multilingual(sentence, low_memory=low_memory)