# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试 detect_multilingual 函数
print(detect_multilingual("Hello, world!你好世界!Привет, мир!Hola mundo!Ciao mondo!Olá mundo!Merhaba dünya!"))

# 测试 detect 函数
print(detect("hello world"))  # 测试英语
print(detect("Привет, мир!"))  # 测试俄语
print(detect("こんにちは世界"))  # 测试日语
print(detect("안녕하세요 세계"))  # 测试韩语
print(detect("Bonjour le monde"))  # 测试法语
print(detect("Hallo Welt"))  # 测试德语

# 测试 detect_language 函数
print(detect_language("hello world"))  # 测试英语
print(detect_language("你好世界"))  # 测试简体中文
print(detect_language("こんにちは世界"))  # 测试日语
print(detect_language("안녕하세요 세계"))  # 测试韩语
print(detect_language("Bonjour le monde"))  # 测试法语
print(detect_language("Hallo Welt"))  # 测试德语