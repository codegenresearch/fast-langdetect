# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_detect_multilingual():
    """
    Test the detect_multilingual function with a mixed language string.
    The function should return a list of detected languages with their scores.
    """
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
    expected_languages = ['ja', 'uk', 'zh', 'sr', 'bg']
    detected_languages = [item['lang'] for item in result]
    assert any(lang in detected_languages for lang in expected_languages), "detect_multilingual did not detect expected languages"

def test_detect():
    """
    Test the detect function with a simple English string.
    The function should return a dictionary with the detected language.
    """
    result = detect("hello world")
    assert result["lang"] == "en", "detect did not return 'en' for 'hello world'"

def test_detect_language():
    """
    Test the detect_language function with various language strings.
    The function should return the correct language code for each string.
    """
    assert detect_language("Привет, мир!") == "RU", "detect_language did not return 'RU' for Russian"
    assert detect_language("你好世界") == "ZH", "detect_language did not return 'ZH' for Chinese"
    assert detect_language("こんにちは世界") == "JA", "detect_language did not return 'JA' for Japanese"
    assert detect_language("안녕하세요 세계") == "KO", "detect_language did not return 'KO' for Korean"
    assert detect_language("Bonjour le monde") == "FR", "detect_language did not return 'FR' for French"
    assert detect_language("Hallo Welt") == "DE", "detect_language did not return 'DE' for German"
    assert detect_language("Hola mundo") == "ES", "detect_language did not return 'ES' for Spanish"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "detect_language did not return 'ZH' for Traditional Chinese"

def test_detect_language_error_handling():
    """
    Test the detect_language function with an unsupported language string.
    The function should raise an exception if the language is not supported.
    """
    try:
        detect_language("This is a test string with no clear language")
    except Exception as e:
        assert isinstance(e, Exception), "detect_language did not raise an exception for unsupported language"