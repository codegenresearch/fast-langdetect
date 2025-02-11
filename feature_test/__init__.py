# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_langs
from fast_langdetect import parse_sentence

# Testing sentence parsing
print(parse_sentence("你好世界"))  # Expected output: parsed sentence structure
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))  # Expected output: parsed sentence structure

# Testing multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Expected output: list of detected languages

# Testing single language detection
print(detect("hello world"))  # Expected output: 'en'
print(detect("你好世界"))  # Expected output: 'zh'
print(detect("こんにちは世界"))  # Expected output: 'ja'
print(detect("안녕하세요 세계"))  # Expected output: 'ko'
print(detect("Bonjour le monde"))  # Expected output: 'fr'
print(detect("Hallo Welt"))  # Expected output: 'de'
print(detect("これらの機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: 'zh'

# Testing language probabilities
print(detect_langs("Привет, мир!"))  # Expected output: list of languages with probabilities