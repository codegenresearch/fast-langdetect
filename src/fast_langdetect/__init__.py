# -*- coding: utf-8 -*-

from fast_langdetect import detect, detect_multilingual, detect_language

# 添加更多的语言检测示例和测试用例以提高覆盖率

def test_multilingual_detection():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_single_language_detection():
    assert detect("hello world")["lang"] == "en", "Language detection error"
    assert detect("你好世界")["lang"] == "zh", "Language detection error"
    assert detect("こんにちは世界")["lang"] == "ja", "Language detection error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection error"
    assert detect("Bonjour le monde")["lang"] == "fr", "Language detection error"

def test_language_code_detection():
    assert detect_language("hello world") == "EN", "Language code detection error"
    assert detect_language("你好世界") == "ZH", "Language code detection error"
    assert detect_language("こんにちは世界") == "JA", "Language code detection error"
    assert detect_language("안녕하세요 세계") == "KO", "Language code detection error"
    assert detect_language("Bonjour le monde") == "FR", "Language code detection error"
    assert detect_language("Hallo Welt") == "DE", "Language code detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language code detection error"

# 添加更多语言的测试用例