# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

"""
This module contains test functions to verify the language detection capabilities of the fast_langdetect library.
It includes tests for single language detection, multilingual detection, and case-insensitive language detection.
"""

def test_muti_detect():
    """
    Test the multilingual detection feature of the fast_langdetect library.
    This function checks if the library can correctly identify multiple languages in a single string.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    # Expected output: [{'lang': 'ja', 'score': ...}, {'lang': 'uk', 'score': ...}, {'lang': 'zh', 'score': ...}]
    print("Multilingual detection result:", result)
    assert any(item.get("lang") == "ja" for item in result), "Japanese not detected"
    assert any(item.get("lang") == "uk" for item in result), "Ukrainian not detected"
    assert any(item.get("lang") == "zh" for item in result), "Chinese not detected"

def test_detect():
    """
    Test the single language detection feature of the fast_langdetect library.
    This function checks if the library can correctly identify the language of a single string.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "English detection failed"
    assert detect("你好世界")["lang"] == "zh", "Chinese detection failed"
    assert detect("こんにちは世界")["lang"] == "ja", "Japanese detection failed"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Korean detection failed"
    assert detect("Bonjour le monde")["lang"] == "fr", "French detection failed"
    assert detect("Hallo Welt")["lang"] == "de", "German detection failed"
    assert detect("Hola mundo")["lang"] == "es", "Spanish detection failed"
    print("Single language detection tests passed.")

def test_detect_totally():
    """
    Test the case-insensitive language detection feature of the fast_langdetect library.
    This function checks if the library can correctly identify the language of a string and return the language code in uppercase.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "English detection failed"
    assert detect_language("你好世界") == "ZH", "Chinese detection failed"
    assert detect_language("こんにちは世界") == "JA", "Japanese detection failed"
    assert detect_language("안녕하세요 세계") == "KO", "Korean detection failed"
    assert detect_language("Bonjour le monde") == "FR", "French detection failed"
    assert detect_language("Hallo Welt") == "DE", "German detection failed"
    assert detect_language("Hola mundo") == "ES", "Spanish detection failed"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH", "Chinese detection failed"
    print("Case-insensitive language detection tests passed.")