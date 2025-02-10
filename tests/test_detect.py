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
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    assert 'en' in [lang['lang'] for lang in result]
    assert 'zh' in [lang['lang'] for lang in result]
    assert 'uk' in [lang['lang'] for lang in result]

def test_detect():
    """
    Test the detect function to ensure it correctly identifies the primary language of a string.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en"
    assert detect("你好世界")["lang"] == "zh"
    assert detect("こんにちは世界")["lang"] == "ja"
    assert detect("안녕하세요 세계")["lang"] == "ko"
    assert detect("Bonjour le monde")["lang"] == "fr"
    assert detect("Hallo Welt")["lang"] == "de"
    assert detect("Hola mundo")["lang"] == "es"

def test_detect_totally():
    """
    Test the detect_language function to ensure it correctly identifies the language of a string with a simplified output.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN"
    assert detect_language("你好世界") == "ZH"
    assert detect_language("こんにちは世界") == "JA"
    assert detect_language("안녕하세요 세계") == "KO"
    assert detect_language("Bonjour le monde") == "FR"
    assert detect_language("Hallo Welt") == "DE"
    assert detect_language("Hola mundo") == "ES"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH"

def test_failed_example():
    """
    Test the error handling of the detect function with an empty string.
    """
    from fast_langdetect import detect
    try:
        detect("")
    except ValueError:
        pass
    else:
        assert False


This code snippet addresses the feedback by:
1. Correcting the unterminated string literal in the comments.
2. Simplifying the assertions to match the gold code style.
3. Ensuring the test cases are consistent with the gold code.
4. Adjusting the exception handling in the `test_failed_example` function to check for a specific `ValueError`.
5. Maintaining consistent formatting and comments throughout the code.
6. Ensuring language codes are consistent with those in the gold code.