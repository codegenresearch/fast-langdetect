# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect_language, detect_multilingual

# Testing multilingual detection
# Expected output: list of dictionaries with language and score
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]

# Testing single language detection
print(detect_language("hello world"))  # Expected output: 'en'
print(detect_language("你好世界"))  # Expected output: 'zh'
print(detect_language("こんにちは世界"))  # Expected output: 'ja'
print(detect_language("안녕하세요 세계"))  # Expected output: 'ko'
print(detect_language("Bonjour le monde"))  # Expected output: 'fr'
print(detect_language("Hallo Welt"))  # Expected output: 'de'
print(detect_language("Esto es una prueba en español"))  # Expected output: 'es'
print(detect_language("これらの機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: 'zh'
print(detect_language("Ciao, mondo"))  # Expected output: 'it'
print(detect_language("Olá, mundo"))  # Expected output: 'pt'
print(detect_language("Привет, мир!"))  # Expected output: 'ru'
print(detect_language("Bonjour tout le monde"))  # Expected output: 'fr'
print(detect_language("Hallo alle Welt"))  # Expected output: 'de'
print(detect_language("Olá a todos"))  # Expected output: 'pt'
print(detect_language("Привет всем"))  # Expected output: 'ru'
print(detect_language("Ciao a tutti"))  # Expected output: 'it'