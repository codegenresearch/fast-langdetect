# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    """
    Test the detect_multilingual function with low memory mode enabled.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error: Expected 'en' for 'hello world'"

def test_detect():
    """
    Test the detect function for various languages.
    """
    from fast_langdetect import detect
    assert detect("hello world", low_memory=True)["lang"] == "en", "ft_detect error: Expected 'en' for 'hello world'"
    assert detect("你好世界", low_memory=True)["lang"] == "zh", "ft_detect error: Expected 'zh' for '你好世界'"
    assert detect("こんにちは世界", low_memory=True)["lang"] == "ja", "ft_detect error: Expected 'ja' for 'こんにちは世界'"
    assert detect("안녕하세요 세계", low_memory=True)["lang"] == "ko", "ft_detect error: Expected 'ko' for '안녕하세요 세계'"
    assert detect("Bonjour le monde", low_memory=True)["lang"] == "fr", "ft_detect error: Expected 'fr' for 'Bonjour le monde'"

def test_detect_totally():
    """
    Test the detect_language function for various languages.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world", low_memory=True) == "en", "ft_detect error: Expected 'en' for 'hello world'"
    assert detect_language("你好世界", low_memory=True) == "zh", "ft_detect error: Expected 'zh' for '你好世界'"
    assert detect_language("こんにちは世界", low_memory=True) == "ja", "ft_detect error: Expected 'ja' for 'こんにちは世界'"
    assert detect_language("안녕하세요 세계", low_memory=True) == "ko", "ft_detect error: Expected 'ko' for '안녕하세요 세계'"
    assert detect_language("Bonjour le monde", low_memory=True) == "fr", "ft_detect error: Expected 'fr' for 'Bonjour le monde'"
    assert detect_language("Hallo Welt", low_memory=True) == "de", "ft_detect error: Expected 'de' for 'Hallo Welt'"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等",
        low_memory=True
    ) == "zh", "ft_detect error: Expected 'zh' for the given Chinese text"