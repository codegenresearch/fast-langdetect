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


def test_language_detection():
    from fast_langdetect import detect_multilingual
    from fast_langdetect import detect

    # Test Japanese detection
    assert detect_language("こんにちは世界") == "JA"
    assert detect_language("こんにちは世界", low_memory=False) == "JA"
    assert detect_language("こんにちは世界", low_memory=True) == "JA"

    # Test other languages
    assert detect_language("Hello, world!") == "EN"
    assert detect_language("你好世界") == "ZH"
    assert detect_language("안녕하세요 세계") == "KO"
    assert detect_language("Bonjour le monde") == "FR"
    assert detect_language("Hallo Welt") == "DE"
    assert detect_language("Hola mundo") == "ES"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH"

    # Test multilingual detection
    result = detect_multilingual("Hello, world!你好世界Привет, мир!", low_memory=True)
    assert any(item['lang'] == 'ja' for item in result), "JA language not detected"
    assert any(item['lang'] == 'zh' for item in result), "ZH language not detected"
    assert any(item['lang'] == 'ru' for item in result), "RU language not detected"
    assert any(item['lang'] == 'en' for item in result), "EN language not detected"

    print("All tests passed!")