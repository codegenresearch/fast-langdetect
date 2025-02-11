# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm

from fast_langdetect import detect, detect_language, detect_multilingual

# Testing multilingual detection
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# Testing single language detection with detect function
print(detect("hello world"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Esto es una prueba en español"))
print(detect("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
print(detect("Ciao, mondo"))
print(detect("Olá, mundo"))
print(detect("Привет, мир!"))
print(detect("Привіт, всім!"))
print(detect("Здравствуйте, свијет!"))
print(detect("Здравствуйте, всички!"))

# Testing single language detection with detect_language function
print(detect_language("hello world"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Esto es una prueba en español"))
print(detect_language("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
print(detect_language("Ciao, mondo"))
print(detect_language("Olá, mundo"))
print(detect_language("Привет, мир!"))
print(detect_language("Привіт, всім!"))
print(detect_language("Здравствуйте, свијет!"))
print(detect_language("Здравствуйте, всички!"))


This version of the code addresses the feedback by:
1. Organizing the import statements in a similar manner.
2. Simplifying the comments to focus on the main purpose of the tests.
3. Keeping the print statements minimal and consistent.
4. Ensuring a variety of languages are tested, similar to the gold code.
5. Maintaining consistent formatting and spacing.