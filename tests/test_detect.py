# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    from fast_langdetect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"

def test_detect():
    from fast_langdetect import detect_language
    assert detect_language("hello world").upper() == "EN", "ft_detect error"
    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계").upper() == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde").upper() == "FR", "ft_detect error"
    assert detect_language("Hallo Welt").upper() == "DE", "ft_detect error"
    assert detect_language("Hola mundo").upper() == "ES", "ft_detect error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "ft_detect error"