# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language, parse_sentence

# Testing parse_sentence function
print(parse_sentence("你好世界"))  # Testing Chinese
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))  # Testing mixed languages: Chinese, English, Russian

# Testing detect_multilingual function
# Expected output: [{'lang': 'en', 'prob': ...}, {'lang': 'zh', 'prob': ...}, {'lang': 'ru', 'prob': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Testing mixed languages: English, Chinese, Russian

# Testing detect function
print(detect("hello world"))  # Testing English
print(detect("Привет, мир!"))  # Testing Russian
print(detect("こんにちは世界"))  # Testing Japanese
print(detect("안녕하세요 세계"))  # Testing Korean
print(detect("Bonjour le monde"))  # Testing French
print(detect("Hallo Welt"))  # Testing German
print(detect("Hola mundo"))  # Testing Spanish

# Testing detect_language function
print(detect_language("hello world"))  # Testing English, expected output: 'EN'
print(detect_language("你好世界"))  # Testing Chinese, expected output: 'ZH'
print(detect_language("こんにちは世界"))  # Testing Japanese, expected output: 'JA'
print(detect_language("안녕하세요 세계"))  # Testing Korean, expected output: 'KO'
print(detect_language("Bonjour le monde"))  # Testing French, expected output: 'FR'
print(detect_language("Hallo Welt"))  # Testing German, expected output: 'DE'
print(detect_language("Hola mundo"))  # Testing Spanish, expected output: 'ES'