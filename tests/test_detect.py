# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm
import warnings

warnings.warn("The function `detect_langs` is deprecated. Use `detect_multiple_languages` instead.", DeprecationWarning)

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual as detect_multiple_languages
    result = detect_multiple_languages("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    from fast_langdetect.ft_detect import detect
    assert detect("hello world") == "en", "ft_detect error"
    assert detect("你好世界") == "zh", "ft_detect error"
    assert detect("こんにちは世界") == "ja", "ft_detect error"
    assert detect("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect("Bonjour le monde") == "fr", "ft_detect error"
    assert detect("Hallo Welt") == "de", "ft_detect error"
    assert detect("Hola mundo") == "es", "ft_detect error"
    assert detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "ft_detect error"

def test_detect_totally():
    from fast_langdetect.ft_detect import detect
    assert detect("hello world") == "en", "ft_detect error"
    assert detect("你好世界") == "zh", "ft_detect error"
    assert detect("こんにちは世界") == "ja", "ft_detect error"
    assert detect("안녕하세요 세계") == "ko", "ft_detect error"
    assert detect("Bonjour le monde") == "fr", "ft_detect error"
    assert detect("Hallo Welt") == "de", "ft_detect error"
    assert detect("Hola mundo") == "es", "ft_detect error"
    assert detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "ft_detect error"


This code snippet addresses the feedback by:
1. Renaming the function names to match the gold code (`test_muti_detect` and `test_detect`).
2. Ensuring the import statements align with the gold code.
3. Directly comparing the return values to the expected language codes without using `.lower()` or `.upper()`.
4. Using "ft_detect error" for assertion messages.
5. Keeping both `test_muti_detect` and `test_detect_totally` functions to cover all cases.