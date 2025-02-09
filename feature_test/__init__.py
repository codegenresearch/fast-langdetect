# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# Test detect_multilingual function
# Expected output: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Test mixed languages: English, Chinese, Russian

# Test detect function
print(detect("hello world"))  # Test English, expected output: 'en'
print(detect("Привет, мир!"))  # Test Russian, expected output: 'ru'
print(detect("こんにちは世界"))  # Test Japanese, expected output: 'ja'
print(detect("안녕하세요 세계"))  # Test Korean, expected output: 'ko'
print(detect("Bonjour le monde"))  # Test French, expected output: 'fr'
print(detect("Hallo Welt"))  # Test German, expected output: 'de'
print(detect("Hola mundo"))  # Test Spanish, expected output: 'es'
print(detect("Ciao mondo"))  # Test Italian, expected output: 'it'
print(detect("Olá mundo"))  # Test Portuguese, expected output: 'pt'
print(detect("Merhaba dünya"))  # Test Turkish, expected output: 'tr'
print(detect("你好，世界！Hello, world！Привет, мир！"))  # Test mixed languages: Simplified Chinese, English, Russian

# Test detect_language function
print(detect_language("hello world"))  # Test English, expected output: 'EN'
print(detect_language("你好世界"))  # Test Simplified Chinese, expected output: 'ZH'
print(detect_language("こんにちは世界"))  # Test Japanese, expected output: 'JA'
print(detect_language("안녕하세요 세계"))  # Test Korean, expected output: 'KO'
print(detect_language("Bonjour le monde"))  # Test French, expected output: 'FR'
print(detect_language("Hallo Welt"))  # Test German, expected output: 'DE'
print(detect_language("Hola mundo"))  # Test Spanish, expected output: 'ES'
print(detect_language("Ciao mondo"))  # Test Italian, expected output: 'IT'
print(detect_language("Olá mundo"))  # Test Portuguese, expected output: 'PT'
print(detect_language("Merhaba dünya"))  # Test Turkish, expected output: 'TR'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Test Traditional Chinese, expected output: 'ZH'