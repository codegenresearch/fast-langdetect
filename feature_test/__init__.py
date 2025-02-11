# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多种语言的检测
# Testing language detection for various languages

# Example usage of the functions
print("Detecting single language:")
print(detect("hello world"))  # Expected output: 'en'
print(detect_language("hello world"))  # Expected output: 'EN'
print(detect("こんにちは世界"))  # Expected output: 'ja'
print(detect_language("こんにちは世界"))  # Expected output: 'JA'
print(detect("안녕하세요 세계"))  # Expected output: 'ko'
print(detect_language("안녕하세요 세계"))  # Expected output: 'KO'
print(detect("Bonjour le monde"))  # Expected output: 'fr'
print(detect_language("Bonjour le monde"))  # Expected output: 'FR'
print(detect("Привет, мир!"))  # Expected output: 'ru'
print(detect_language("Привет, мир!"))  # Expected output: 'RU'
print(detect("你好，世界！"))  # Expected output: 'zh'
print(detect_language("你好，世界！"))  # Expected output: 'ZH'
print(detect("¡Hola, mundo!"))  # Expected output: 'es'
print(detect_language("¡Hola, mundo!"))  # Expected output: 'ES'
print(detect("Hallo Welt"))  # Expected output: 'de'
print(detect_language("Hallo Welt"))  # Expected output: 'DE'
print(detect("Cześć świecie"))  # Expected output: 'pl'
print(detect_language("Cześć świecie"))  # Expected output: 'PL'
print(detect("Olá, mundo"))  # Expected output: 'pt'
print(detect_language("Olá, mundo"))  # Expected output: 'PT'

print("\nDetecting multiple languages:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Bonjour le monde!こんにちは世界!안녕하세요 세계!"))
# Expected output: [{'lang': 'fr', 'score': ...}, {'lang': 'ja', 'score': ...}, {'lang': 'ko', 'score': ...}]
print(detect_multilingual("Hallo Welt!Cześć świecie!Olá, mundo!"))
# Expected output: [{'lang': 'de', 'score': ...}, {'lang': 'pl', 'score': ...}, {'lang': 'pt', 'score': ...}]
print(detect_multilingual("¡Hola, mundo!Bonjour le monde!Привет, мир!"))
# Expected output: [{'lang': 'es', 'score': ...}, {'lang': 'fr', 'score': ...}, {'lang': 'ru', 'score': ...}]


This code snippet addresses the feedback by:
1. Ensuring the output of `detect_multilingual` includes both the language and the score.
2. Adding more diverse examples to showcase the functionality of the `detect_language` method.
3. Including a comment in Chinese to describe the languages being tested.
4. Double-checking to ensure only necessary imports are included.
5. Organizing the code with a clear flow and logical order.