# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect_languages, detect_multiple_languages, parse_text

# Example usage of the new function names
print(parse_text("你好世界"))
print(parse_text("你好世界！Hello, world！Привет, мир！"))
print(detect_multiple_languages("Hello, world!你好世界!Привет, мир!"))

print(detect_languages("hello world"))
print(detect_multiple_languages("Привет, мир!"))