# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
import logging
from fast_langdetect import detect as detect_language, detect_multilingual as detect_multiple_languages, detect_langs as detect_languages
from fast_langdetect import parse_sentence

# Logging for deprecated functions
logging.warning("The function 'parse_sentence' is deprecated. Consider using 'detect_language' or 'detect_multiple_languages' for better functionality.")

print(parse_sentence("你好世界"))
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))
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