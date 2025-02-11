# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """
    Test the detect_multilingual function.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world")
    assert result[0].get("lang") == "en", "Test failed for 'hello world'"

def test_detect():
    """
    Test the detect function for various languages.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "Test failed"
    assert detect("你好世界")["lang"] == "zh", "Test failed"
    assert detect("こんにちは世界")["lang"] == "ja", "Test failed"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Test failed"
    assert detect("Bonjour le monde")["lang"] == "fr", "Test failed"

def test_detect_totally():
    """
    Test the detect_language function for various languages.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "Test failed"
    assert detect_language("你好世界") == "ZH", "Test failed"
    assert detect_language("こんにちは世界") == "JA", "Test failed"
    assert detect_language("안녕하세요 세계") == "KO", "Test failed"
    assert detect_language("Bonjour le monde") == "FR", "Test failed"
    assert detect_language("Hallo Welt") == "DE", "Test failed"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH", "Test failed"

def test_failed_example():
    """
    Test the detect_language function for a case that should raise an exception.
    """
    from fast_langdetect import detect_language
    try:
        detect_language("")
        assert False, "Expected an exception for empty string"
    except Exception as e:
        assert str(e) == "No language detected", "Expected 'No language detected' exception for empty string"


This code addresses the feedback by:
1. Removing the invalid line that caused the syntax error.
2. Simplifying the error messages in assertions to be more concise and consistent.
3. Ensuring that the language codes returned by the `detect_language` function are in uppercase.
4. Keeping import statements consistent and placing them at the top of the function where they are used.
5. Making the docstrings more concise and aligned with the gold code's style.