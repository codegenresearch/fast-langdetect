# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual

# 测试多语言检测
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # 测试多语言检测

# 测试单语言检测
print(detect("hello world"))  # 测试英文检测
print(detect("Привет, мир!"))  # 测试俄文检测
print(detect("こんにちは世界"))  # 测试日文检测
print(detect("안녕하세요 세계"))  # 测试韩文检测
print(detect("Bonjour le monde"))  # 测试法文检测
print(detect("Hallo Welt"))  # 测试德文检测
print(detect("Esto es una prueba en español"))  # 测试西班牙文检测
print(detect("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # 测试中文检测

# 测试混合语言检测
print(detect("こんにちは世界！안녕하세요 세계！Bonjour le monde！Hallo Welt"))  # 测试混合语言检测