# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect.ft_detect import detect_multilingual
from fast_langdetect import detect, detect_language

def test_muti_detect():
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    # Test detect function
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"

def test_detect_totally():
    # Test detect_language function
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Привет, мир!") == "RU", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("Hola mundo") == "ES", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"


### Changes Made:
1. **Import Statements**: Moved the import statements to the top of the file to improve readability and performance.
2. **Assertion Consistency**: Ensured that the language codes in the assertions match the expected output exactly, including the case.
3. **Comment Clarity**: Kept necessary comments concise and relevant.
4. **Formatting**: Ensured that long strings are formatted similarly to the gold code.
5. **Redundant Assertions**: Removed duplicate assertions to ensure each test case is unique and necessary.