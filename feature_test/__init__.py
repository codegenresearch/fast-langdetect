# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect as detect_language, detect_multilingual as detect_multiple_languages, detect_langs as detect_languages

# Example usage of the functions
print(detect_multiple_languages("Hello, world!你好世界!Привет, мир!"))
print(detect_language("hello world"))
print(detect_languages("Привет, мир!"))

# Additional test cases for better coverage
assert detect_language("bonjour le monde") == "FR", "Language detection error for French"
assert detect_language("こんにちは世界") == "JA", "Language detection error for Japanese"
assert detect_language("안녕하세요 세계") == "KO", "Language detection error for Korean"
assert detect_language("Hallo Welt") == "DE", "Language detection error for German"
assert detect_language("Cześć świecie") == "PL", "Language detection error for Polish"
assert detect_language("Olá, mundo") == "PT", "Language detection error for Portuguese"
assert detect_language("Привет, мир!") == "RU", "Language detection error for Russian"
assert detect_language("你好，世界！") == "ZH", "Language detection error for Chinese"
assert detect_language("Bonjour le monde") == "FR", "Language detection error for French"
assert detect_language("こんにちは") == "JA", "Language detection error for Japanese"
assert detect_language("안녕하세요") == "KO", "Language detection error for Korean"
assert detect_language("Hallo") == "DE", "Language detection error for German"
assert detect_language("Cześć") == "PL", "Language detection error for Polish"
assert detect_language("Olá") == "PT", "Language detection error for Portuguese"
assert detect_language("Привет") == "RU", "Language detection error for Russian"
assert detect_language("你好") == "ZH", "Language detection error for Chinese"