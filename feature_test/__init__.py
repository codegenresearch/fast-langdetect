# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, parse_sentence

# Testing parse_sentence function
print(parse_sentence("你好世界"))  # Testing Chinese
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))  # Testing mixed languages

# Testing detect_multilingual function
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Testing mixed languages

# Testing detect function
print(detect("hello world"))  # Testing English
print(detect("Привет, мир!"))  # Testing Russian