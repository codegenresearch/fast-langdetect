# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多语言检测
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # 多语言检测: 英文, 中文, 俄文

# 测试单语言检测
print(detect("hello world"))  # 测试英文检测
print(detect_language("Привет, мир!"))  # 测试俄文检测
print(detect_language("こんにちは世界"))  # 测试日文检测
print(detect_language("안녕하세요 세계"))  # 测试韩文检测
print(detect_language("Bonjour le monde"))  # 测试法文检测
print(detect_language("Hallo Welt"))  # 测试德文检测
print(detect_language("Hola mundo"))  # 测试西班牙文检测
print(detect_language("你好世界"))  # 测试简体中文检测
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # 测试繁体中文检测

# 测试混合语言检测
print(detect_language("こんにちは世界！안녕하세요 세계！Bonjour le monde！Hallo Welt"))  # 混合语言检测