# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm
import warnings
from fast_langdetect import detect_multiple_languages, detect_language

warnings.warn("The function `detect_langs` is deprecated. Use `detect_multiple_languages` instead.", DeprecationWarning)

def test_detect_multiple_languages():
    result = detect_multiple_languages("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_detect_single_language():
    assert detect_language("hello world") == "en", "Language detection error"
    assert detect_language("你好世界") == "zh", "Language detection error"
    assert detect_language("こんにちは世界") == "ja", "Language detection error"