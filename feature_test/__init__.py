# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多种语言混合的句子
# Expected: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# 测试单一语言的句子
# Expected: en
print(detect("hello world"))

# Expected: zh
print(detect("你好世界"))

# Expected: ja
print(detect("こんにちは世界"))

# Expected: ko
print(detect("안녕하세요 세계"))

# Expected: fr
print(detect("Bonjour le monde"))

# Expected: de
print(detect("Hallo Welt"))

# Expected: es
print(detect("Hola mundo"))

# 测试 detect_language 函数
# Expected: EN
print(detect_language("hello world"))

# Expected: ZH
print(detect_language("你好世界"))

# Expected: JA
print(detect_language("こんにちは世界"))

# Expected: KO
print(detect_language("안녕하세요 세계"))

# Expected: FR
print(detect_language("Bonjour le monde"))

# Expected: DE
print(detect_language("Hallo Welt"))

# Expected: ES
print(detect_language("Hola mundo"))

# Expected: ZH
print(detect_language("これらの機構主辦の課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))