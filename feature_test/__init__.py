# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language
from fast_langdetect import parse_sentence

# Testing sentence parsing
print(parse_sentence("你好世界"))  # Expected: Chinese
print(parse_sentence("你好世界！Hello, world！Привет, мир！"))  # Expected: Mixed languages

# Testing multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # Expected: List of detected languages

# Testing single language detection
print(detect("hello world"))  # Expected: English
print(detect("你好世界"))  # Expected: Chinese
print(detect("こんにちは世界"))  # Expected: Japanese
print(detect("안녕하세요 세계"))  # Expected: Korean
print(detect("Bonjour le monde"))  # Expected: French
print(detect("Hallo Welt"))  # Expected: German

# Testing language detection with detect_language
print(detect_language("hello world"))  # Expected: EN
print(detect_language("你好世界"))  # Expected: ZH
print(detect_language("こんにちは世界"))  # Expected: JA
print(detect_language("안녕하세요 세계"))  # Expected: KO
print(detect_language("Bonjour le monde"))  # Expected: FR
print(detect_language("Hallo Welt"))  # Expected: DE
print(detect_language("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected: ZH