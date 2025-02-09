# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
import warnings
from fast_langdetect import detect as deprecated_detect, detect_multilingual as deprecated_detect_multilingual, detect_langs as deprecated_detect_langs
from fast_langdetect import parse_sentence

def detect_languages(text, low_memory=False):
    warnings.warn("The `detect_languages` function is the new consolidated method for language detection. Old functions are deprecated.", DeprecationWarning)
    if low_memory:
        return deprecated_detect_multilingual(text)
    else:
        return deprecated_detect_langs(text)

print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_languages("Hello, world!你好世界!Привет, мир!", low_memory=True))

print(detect_languages("hello world"))
print(detect_languages("Привет, мир!"))