# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

"""
This module contains test functions to verify the functionality of the fast_langdetect library.
It includes tests for detecting multiple languages in a single string, detecting the primary language,
and detecting the language with a simplified output.

Example Usage:
--------------
# Detect multiple languages in a single string
result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
print(result)  # Output: [{'lang': 'ja', 'score': ...}, {'lang': 'uk', 'score': ...}, ...]

# Detect the primary language of a string
language = detect("hello world")
print(language)  # Output: {'lang': 'en', 'score': ...}

# Detect the language with a simplified output
language_code = detect_language("Привет, мир!")
print(language_code)  # Output: 'RU'
"""

def test_muti_detect():
    """
    Test the detect_multilingual function to ensure it correctly identifies multiple languages in a single string.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    assert result[0].get("lang") == "ja", "ft_detect error"
    assert result[1].get("lang") == "uk", "ft_detect error"
    assert result[2].get("lang") == "zh", "ft_detect error"

def test_detect():
    """
    Test the detect function to ensure it correctly identifies the primary language of a string.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error"

def test_detect_totally():
    """
    Test the detect_language function to ensure it correctly identifies the language of a string with a simplified output.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("Hola mundo") == "ES", "ft_detect error"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH", "ft_detect error"