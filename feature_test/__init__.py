# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Testing multilingual detection
# Expected output: list of dictionaries with language and score
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]

# Testing single language detection with detect function
# Expected output: language code
print(detect("hello world"))  # Expected output: 'en'
print(detect("你好世界"))  # Expected output: 'zh'
print(detect("こんにちは世界"))  # Expected output: 'ja'
print(detect("안녕하세요 세계"))  # Expected output: 'ko'
print(detect("Bonjour le monde"))  # Expected output: 'fr'
print(detect("Hallo Welt"))  # Expected output: 'de'
print(detect("Esto es una prueba en español"))  # Expected output: 'es'
print(detect("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: 'zh'
print(detect("Ciao, mondo"))  # Expected output: 'it'
print(detect("Olá, mundo"))  # Expected output: 'pt'
print(detect("Привет, мир!"))  # Expected output: 'ru'
print(detect("Привіт, всім!"))  # Expected output: 'uk'
print(detect("Здравствуйте, свијет!"))  # Expected output: 'sr'
print(detect("Здравствуйте, всички!"))  # Expected output: 'bg'

# Testing single language detection with detect_language function
# Expected output: uppercase language code
print(detect_language("hello world"))  # Expected output: 'EN'
print(detect_language("你好世界"))  # Expected output: 'ZH'
print(detect_language("こんにちは世界"))  # Expected output: 'JA'
print(detect_language("안녕하세요 세계"))  # Expected output: 'KO'
print(detect_language("Bonjour le monde"))  # Expected output: 'FR'
print(detect_language("Hallo Welt"))  # Expected output: 'DE'
print(detect_language("Esto es una prueba en español"))  # Expected output: 'ES'
print(detect_language("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected output: 'ZH'
print(detect_language("Ciao, mondo"))  # Expected output: 'IT'
print(detect_language("Olá, mundo"))  # Expected output: 'PT'
print(detect_language("Привет, мир!"))  # Expected output: 'RU'
print(detect_language("Привіт, всім!"))  # Expected output: 'UK'
print(detect_language("Здравствуйте, свијет!"))  # Expected output: 'SR'
print(detect_language("Здравствуйте, всички!"))  # Expected output: 'BG'


This version of the code addresses the feedback by organizing the import statements, adding comments to summarize the tests, ensuring consistent expected outputs, and maintaining a consistent formatting style.