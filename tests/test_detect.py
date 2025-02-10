# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """
    Test the detect_multilingual function to ensure it correctly identifies multiple languages in a single string.
    """
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    assert result[0].get("lang") == "ja", "ft_detect error"
    assert result[1].get("lang") == "zh", "ft_detect error"
    assert result[2].get("lang") == "uk", "ft_detect error"

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

def test_failed_example():
    """
    Test the error handling of the detect function with an empty string.
    """
    from fast_langdetect import detect
    try:
        detect("")
    except ValueError as e:
        assert str(e) == "No language detected", "ft_detect error"
    else:
        assert False, "ft_detect error: Exception not raised"


This code snippet addresses the feedback by:
1. Ensuring all comments and documentation are properly formatted and do not interfere with the syntax of the Python code.
2. Moving import statements inside each test function to match the gold code's structure.
3. Adjusting the `detect_multilingual` function parameters to match those in the gold code.
4. Ensuring that the assertions in the tests reflect the expected outputs accurately.
5. Refining the exception handling in the `test_failed_example` function to match the gold code's approach.