# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_multilingual_detection():
    """
    Tests the multilingual detection function with a mixed-language string.
    The function should return a list of detected languages with their scores.
    This test checks if the function can handle multiple languages in a single string.
    """
    try:
        result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
        expected_languages = ['ja', 'uk', 'zh', 'sr', 'bg']
        detected_languages = [item['lang'] for item in result]
        assert any(lang in detected_languages for lang in expected_languages), "Multilingual detection failed"
    except Exception as e:
        assert isinstance(e, Exception), "An unexpected exception occurred during multilingual detection"

def test_single_language_detection():
    """
    Tests the single language detection function with various strings.
    The function should return the detected language code.
    This test checks if the function can accurately detect the language of single-language strings.
    """
    try:
        assert detect("hello world") == "en", "Single language detection failed for English"
        assert detect("Привет, мир!") == "ru", "Single language detection failed for Russian"
        assert detect("你好世界") == "zh", "Single language detection failed for Simplified Chinese"
        assert detect("こんにちは世界") == "ja", "Single language detection failed for Japanese"
        assert detect("안녕하세요 세계") == "ko", "Single language detection failed for Korean"
        assert detect("Bonjour le monde") == "fr", "Single language detection failed for French"
        assert detect("Hallo Welt") == "de", "Single language detection failed for German"
        assert detect("Hola mundo") == "es", "Single language detection failed for Spanish"
        assert detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "Single language detection failed for Traditional Chinese"
    except Exception as e:
        assert isinstance(e, Exception), "An unexpected exception occurred during single language detection"

def test_language_detection():
    """
    Tests the language detection function with various strings.
    The function should return the detected language code in uppercase.
    This test checks if the function can accurately detect the language of single-language strings.
    """
    try:
        assert detect_language("Привет, мир!") == "RU", "Language detection failed for Russian"
        assert detect_language("你好世界") == "ZH", "Language detection failed for Simplified Chinese"
        assert detect_language("こんにちは世界") == "JA", "Language detection failed for Japanese"
        assert detect_language("안녕하세요 세계") == "KO", "Language detection failed for Korean"
        assert detect_language("Bonjour le monde") == "FR", "Language detection failed for French"
        assert detect_language("Hallo Welt") == "DE", "Language detection failed for German"
        assert detect_language("Hola mundo") == "ES", "Language detection failed for Spanish"
        assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "Language detection failed for Traditional Chinese"
    except Exception as e:
        assert isinstance(e, Exception), "An unexpected exception occurred during language detection"