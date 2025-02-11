# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect_language, detect_multilingual, detect_languages
from fast_langdetect import analyze_sentence

print(analyze_sentence("你好世界"))
print(analyze_sentence("你好世界！Hello, world！Привет, мир！"))
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

print(detect_language("hello world"))
print(detect_languages("Привет, мир!"))