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


def test_languages():
    from fast_langdetect import detect
    assert detect_language("hello world") == "EN"
    assert detect_language("你好世界") == "ZH"
    assert detect_language("こんにちは世界") == "JA"
    assert detect_language("안녕하세요 세계") == "KO"
    assert detect_language("Bonjour le monde") == "FR"
    assert detect_language("Hallo Welt") == "DE"
    assert detect_language("Hola mundo") == "ES"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH"


def test_multilingual_detect():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world, 你好世界, Привет, мир!", low_memory=True)
    assert any(lang.get("lang") == "ja" and lang.get("score") > 0.3 for lang in result), "ft_detect error"
    assert any(lang.get("lang") == "zh" and lang.get("score") > 0.1 for lang in result), "ft_detect error"
    assert any(lang.get("lang") == "en" and lang.get("score") > 0.1 for lang in result), "ft_detect error"