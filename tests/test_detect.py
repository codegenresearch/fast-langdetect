# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_multilingual_detect():
    """\n    Test the multilingual detection function with low memory mode enabled.\n    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Multilingual detection error for 'hello world'"

def test_single_language_detect():
    """\n    Test the single language detection function.\n    """
    from fast_langdetect import detect
    assert detect("hello world", low_memory=True)["lang"] == "en", "Detection error for 'hello world'"
    assert detect("你好世界", low_memory=True)["lang"] == "zh", "Detection error for '你好世界'"
    assert detect("こんにちは世界", low_memory=True)["lang"] == "ja", "Detection error for 'こんにちは世界'"
    assert detect("안녕하세요 세계", low_memory=True)["lang"] == "ko", "Detection error for '안녕하세요 세계'"
    assert detect("Bonjour le monde", low_memory=True)["lang"] == "fr", "Detection error for 'Bonjour le monde'"

def test_detect_language():
    """\n    Test the language detection function that returns language codes in uppercase.\n    """
    from fast_langdetect import detect_language
    assert detect_language("hello world", low_memory=True) == "EN", "Language detection error for 'hello world'"
    assert detect_language("你好世界", low_memory=True) == "ZH", "Language detection error for '你好世界'"
    assert detect_language("こんにちは世界", low_memory=True) == "JA", "Language detection error for 'こんにちは世界'"
    assert detect_language("안녕하세요 세계", low_memory=True) == "KO", "Language detection error for '안녕하세요 세계'"
    assert detect_language("Bonjour le monde", low_memory=True) == "FR", "Language detection error for 'Bonjour le monde'"
    assert detect_language("Hallo Welt", low_memory=True) == "DE", "Language detection error for 'Hallo Welt'"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等",
        low_memory=True
    ) == "ZH", "Language detection error for the provided Chinese text"