# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_langs

# Example usage of the functions
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
print(detect("hello world"))
print(detect_langs("Привет, мир!"))

# 测试多种语言的检测
# Testing language detection for various languages
assert detect("bonjour le monde") == "FR", "Language detection error for French"
assert detect("こんにちは世界") == "JA", "Language detection error for Japanese"
assert detect("안녕하세요 세계") == "KO", "Language detection error for Korean"
assert detect("Hallo Welt") == "DE", "Language detection error for German"
assert detect("Cześć świecie") == "PL", "Language detection error for Polish"
assert detect("Olá, mundo") == "PT", "Language detection error for Portuguese"
assert detect("Привет, мир!") == "RU", "Language detection error for Russian"
assert detect("你好，世界！") == "ZH", "Language detection error for Chinese"

# Additional test cases for better coverage
assert detect("Bonjour le monde") == "FR", "Language detection error for French"
assert detect("こんにちは") == "JA", "Language detection error for Japanese"
assert detect("안녕하세요") == "KO", "Language detection error for Korean"
assert detect("Hallo") == "DE", "Language detection error for German"
assert detect("Cześć") == "PL", "Language detection error for Polish"
assert detect("Olá") == "PT", "Language detection error for Portuguese"
assert detect("Привет") == "RU", "Language detection error for Russian"
assert detect("你好") == "ZH", "Language detection error for Chinese"

# Test cases for detect_multilingual
assert detect_multilingual("Hello, world!你好世界!Привет, мир!") == [{'lang': 'en'}, {'lang': 'zh'}, {'lang': 'ru'}], "Multilingual detection error"
assert detect_multilingual("Bonjour le monde!こんにちは世界!안녕하세요 세계!") == [{'lang': 'fr'}, {'lang': 'ja'}, {'lang': 'ko'}], "Multilingual detection error"
assert detect_multilingual("Hallo Welt!Cześć świecie!Olá, mundo!") == [{'lang': 'de'}, {'lang': 'pl'}, {'lang': 'pt'}], "Multilingual detection error"


This code snippet addresses the feedback by:
1. Importing functions directly without renaming.
2. Using `detect` instead of `detect_language` for consistency.
3. Adding more diverse test cases.
4. Ensuring the output format of `detect_multilingual` matches the expected format.
5. Including a comment in Chinese to describe the languages being tested.