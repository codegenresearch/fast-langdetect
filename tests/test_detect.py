# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm
import warnings

warnings.warn("The function `detect_langs` is deprecated. Use `detect_multiple_languages` instead.", DeprecationWarning)

def test_detect_multiple():
    from fast_langdetect import detect_multilingual as detect_multiple_languages
    result = detect_multiple_languages("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error"

def test_detect_single():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "en", "Language detection error"
    assert detect_language("你好世界") == "zh", "Language detection error"
    assert detect_language("こんにちは世界") == "ja", "Language detection error"
    assert detect_language("안녕하세요 세계") == "ko", "Language detection error"
    assert detect_language("Bonjour le monde") == "fr", "Language detection error"
    assert detect_language("Hallo Welt") == "de", "Language detection error"
    assert detect_language("Hola mundo") == "es", "Language detection error"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "Language detection error"