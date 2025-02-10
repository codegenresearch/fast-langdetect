# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect_multilingual, detect_language, parse_sentence

# Testing sentence parsing
print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))

# Testing multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing single language detection
print(detect_language("hello world"))
print(detect_language("Привет, мир!"))

# Additional test cases to showcase functionality
# Testing various languages
print(detect_language("こんにちは世界"))  # Japanese
print(detect_language("안녕하세요 세계"))  # Korean
print(detect_language("Bonjour le monde"))  # French
print(detect_language("Hallo Welt"))  # German
print(detect_language("こんにちは世界！안녕하세요 세계！Bonjour le monde！Hallo Welt"))  # Mixed languages
print(detect_language("Esto es una prueba en español"))  # Spanish
print(detect_language("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Chinese