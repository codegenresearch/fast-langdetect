# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm


def test_detect_multiple_languages():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection error for 'hello world'"


def test_detect_languages():
    from fast_langdetect import detect_languages
    assert detect_languages("hello world")[0].lang == "en", "Language detection error for 'hello world'"
    assert detect_languages("你好世界")[0].lang == "zh", "Language detection error for '你好世界'"
    assert detect_languages("こんにちは世界")[0].lang == "ja", "Language detection error for 'こんにちは世界'"