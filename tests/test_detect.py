# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    from fast_langdetect.ft_detect import detect
    assert detect("hello world").get("lang") == "en", "ft_detect error"
    assert detect("你好世界").get("lang") == "zh", "ft_detect error"
    assert detect("こんにちは世界").get("lang") == "ja", "ft_detect error"
    assert detect("안녕하세요 세계").get("lang") == "ko", "ft_detect error"
    assert detect("Bonjour le monde").get("lang") == "fr", "ft_detect error"
    assert detect("Hallo Welt").get("lang") == "de", "ft_detect error"
    assert detect("Hola mundo").get("lang") == "es", "ft_detect error"
    assert detect("這些機構主辦的課程，多以基本電腦使用為主，"
                   "例如文書處理、中文輸入、互聯網應用等").get("lang") == "zh", "ft_detect error"

def test_detect_totally():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("Hola mundo") == "ES", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，"
                   "例如文書處理、中文輸入、互聯網應用等") == "ZH", "ft_detect error"