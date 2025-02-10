# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试繁体，简体，日文，英文，韩文，法文，德文，西班牙文

# Test detect_multilingual with a mixed language string
result_multilingual = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
print("Multilingual detection result:", result_multilingual)

# Test detect with a simple English string
result_detect = detect("hello world")
print("Detect result for 'hello world':", result_detect)

# Test detect_language with various language strings
print("Detect language for 'Привет, мир!':", detect_language("Привет, мир!"))
print("Detect language for '你好世界':", detect_language("你好世界"))
print("Detect language for 'こんにちは世界':", detect_language("こんにちは世界"))
print("Detect language for '안녕하세요 세계':", detect_language("안녕하세요 세계"))
print("Detect language for 'Bonjour le monde':", detect_language("Bonjour le monde"))
print("Detect language for 'Hallo Welt':", detect_language("Hallo Welt"))
print("Detect language for 'Hola mundo':", detect_language("Hola mundo"))
print("Detect language for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))


This code directly calls the language detection functions and prints their results, aligning more closely with the gold code. It removes assertions and error handling for unsupported languages, focusing solely on displaying the results.