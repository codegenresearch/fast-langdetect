# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

from fast_langdetect.ft_detect import detect_multilingual
from fast_langdetect import detect, detect_language

def test_muti_detect():
    """
    Test the detect_multilingual function with low memory mode enabled.
    """
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    """
    Test the detect function for various languages.
    """
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error"

def test_detect_totally():
    """
    Test the detect_language function for various languages.
    """
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

def test_failed_example():
    """
    Test the detect function for a case that should raise an exception.
    """
    try:
        detect("")
        assert False, "ft_detect error"
    except ValueError as e:
        assert str(e) == "No language detected", "ft_detect error"


This code addresses the feedback by:
1. Ensuring all comments are properly formatted with `#`.
2. Removing redundant assertions in the `test_detect` function to match the gold code.
3. Adjusting the `test_failed_example` function to test an appropriate scenario that aligns with the gold code.
4. Ensuring consistent formatting, especially for long lines in the `test_detect_totally` function.
5. Placing import statements at the top of the file without additional comments.
6. Ensuring assertion messages are consistent with the gold code.