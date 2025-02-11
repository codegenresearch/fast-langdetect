# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, parse_sentence

# Testing sentence parsing
print(parse_sentence("你好世界"))  # Expected output: parsed sentence structure
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))  # Expected output: parsed sentence structure

# Testing multilingual detection
# Expected output: list of dictionaries with language and score
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]

# Testing single language detection
print(detect("hello world"))  # Expected output: 'en'
print(detect("你好世界"))  # Expected output: 'zh'
print(detect("こんにちは世界"))  # Expected output: 'ja'
print(detect("안녕하세요 세계"))  # Expected output: 'ko'
print(detect("Bonjour le monde"))  # Expected output: 'fr'
print(detect("Hallo Welt"))  # Expected output: 'de'
print(detect("Esto es una prueba en español"))  # Expected output: 'es'
print(detect("これらの機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: 'zh'
print(detect("Ciao, mondo"))  # Expected output: 'it'
print(detect("Olá, mundo"))  # Expected output: 'pt'
print(detect("Привет, мир!"))  # Expected output: 'ru'