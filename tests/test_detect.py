# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm
import warnings
from fast_langdetect import detect_multilingual as detect_multiple_languages, detect_language

warnings.warn("The function `detect_langs` is deprecated. Use `detect_multiple_languages` instead.", DeprecationWarning)

def test_detect_multiple_languages():
    result = detect_multiple_languages("hello world", low_memory=True)
    assert result[0].get("lang").upper() == "EN", "Language detection error: Expected EN, got {}".format(result[0].get("lang"))

def test_detect_single_language():
    assert detect_language("hello world").upper() == "EN", "Language detection error: Expected EN, got {}".format(detect_language("hello world"))
    assert detect_language("你好世界").upper() == "ZH", "Language detection error: Expected ZH, got {}".format(detect_language("你好世界"))
    assert detect_language("こんにちは世界").upper() == "JA", "Language detection error: Expected JA, got {}".format(detect_language("こんにちは世界"))
    assert detect_language("안녕하세요 세계").upper() == "KO", "Language detection error: Expected KO, got {}".format(detect_language("안녕하세요 세계"))
    assert detect_language("Bonjour le monde").upper() == "FR", "Language detection error: Expected FR, got {}".format(detect_language("Bonjour le monde"))
    assert detect_language("Hallo Welt").upper() == "DE", "Language detection error: Expected DE, got {}".format(detect_language("Hallo Welt"))
    assert detect_language("Hola mundo").upper() == "ES", "Language detection error: Expected ES, got {}".format(detect_language("Hola mundo"))
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "Language detection error: Expected ZH, got {}".format(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))