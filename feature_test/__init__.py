# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_langs, parse_sentence

# Testing sentence parsing
print("Parsing sentence '你好世界':", parse_sentence("你好世界"))
print("Parsing sentence '你好世界！Hello, world！Привет, мир！':", parse_sentence("你好世界！Hello, world！Привет, мир！"))

# Testing multilingual detection
print("Detecting languages in 'Hello, world!你好世界!Привет, мир!':", detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing single language detection
print("Detecting language in 'hello world':", detect("hello world"))
print("Detecting languages in 'Привет, мир!':", detect_langs("Привет, мир!"))

# Additional test cases to showcase functionality
print("Detecting language in 'こんにちは世界':", detect("こんにちは世界"))
print("Detecting languages in 'こんにちは世界':", detect_langs("こんにちは世界"))
print("Detecting language in '안녕하세요 세계':", detect("안녕하세요 세계"))
print("Detecting languages in '안녕하세요 세계':", detect_langs("안녕하세요 세계"))
print("Detecting language in 'Bonjour le monde':", detect("Bonjour le monde"))
print("Detecting languages in 'Bonjour le monde':", detect_langs("Bonjour le monde"))
print("Detecting language in 'Hallo Welt':", detect("Hallo Welt"))
print("Detecting languages in 'Hallo Welt':", detect_langs("Hallo Welt"))
print("Detecting language in 'これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
print("Detecting languages in 'これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_langs("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))