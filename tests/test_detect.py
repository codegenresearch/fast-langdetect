# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    print("Multilingual detection result:", result)
    assert any(item.get("lang") == "ja" for item in result), "ft_detect error"
    assert any(item.get("lang") == "uk" for item in result), "ft_detect error"
    assert any(item.get("lang") == "zh" for item in result), "ft_detect error"

def test_detect():
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error"
    print("Single language detection tests passed.")

def test_detect_totally():
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
    print("Case-insensitive language detection tests passed.")

def test_failed_example():
    from fast_langdetect import detect
    try:
        detect(None)
    except Exception as e:
        assert str(e) == "Input text is None", "ft_detect error"
    print("Error handling test passed.")