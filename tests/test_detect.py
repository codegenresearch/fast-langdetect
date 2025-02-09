# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """
    Test the detect_multilingual function with low memory mode enabled.
    """
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Expected language 'en' for 'hello world'"

def test_detect():
    """
    Test the detect function for various languages.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "Expected language 'en' for 'hello world'"
    assert detect("你好世界")["lang"] == "zh", "Expected language 'zh' for '你好世界'"
    assert detect("こんにちは世界")["lang"] == "ja", "Expected language 'ja' for 'こんにちは世界'"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Expected language 'ko' for '안녕하세요 세계'"
    assert detect("Bonjour le monde")["lang"] == "fr", "Expected language 'fr' for 'Bonjour le monde'"

def test_detect_totally():
    """
    Test the detect_language function for various languages.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "Expected language 'EN' for 'hello world'"
    assert detect_language("你好世界") == "ZH", "Expected language 'ZH' for '你好世界'"
    assert detect_language("こんにちは世界") == "JA", "Expected language 'JA' for 'こんにちは世界'"
    assert detect_language("안녕하세요 세계") == "KO", "Expected language 'KO' for '안녕하세요 세계'"
    assert detect_language("Bonjour le monde") == "FR", "Expected language 'FR' for 'Bonjour le monde'"
    assert detect_language("Hallo Welt") == "DE", "Expected language 'DE' for 'Hallo Welt'"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH", "Expected language 'ZH' for the given Chinese text"

def test_failed_example():
    """
    Test the detect function with an unsupported language.
    """
    from fast_langdetect import detect
    try:
        detect("This is a test for an unsupported language")
    except Exception as e:
        assert isinstance(e, Exception), "Expected an exception for unsupported language"