# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午4:00
# @Author  : sudoskys
# @File    : __init__.py
from .infer import detect
from .infer import detect_multilingual  # noqa: F401


def contains_japanese_characters(string):
    """\n    Check if the string contains Japanese characters\n    :param string: str sentence\n    :return: bool\n    """
    for ch in string:
        if 0x3040 < ord(ch) < 0x30FF:
            return True
    return False


def detect_language_code(sentence, *, low_memory: bool = True):
    """\n    Detect language code\n    :param sentence: str sentence\n    :param low_memory: bool (default: True) whether to use low memory mode\n    :return: ZH, EN, JA, KO, FR, DE, ES, .... (two uppercase letters)\n    """
    lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()
    if lang_code == "JA" and not contains_japanese_characters(sentence):
        lang_code = "ZH"
    return lang_code


def test_detect_language_code():
    """\n    Comprehensive tests for language detection\n    """
    assert detect_language_code("hello world") == "EN", "ft_detect error"
    assert detect_language_code("你好世界") == "ZH", "ft_detect error"
    assert detect_language_code("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language_code("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language_code("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language_code("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language_code("Hola mundo") == "ES", "ft_detect error"
    assert detect_language_code("これらの机构主辦的課程，多以基本电脑使用为主，例如文书处理、中文输入、互联网应用等") == "ZH", "ft_detect error"
    # Additional tests for more languages can be added here