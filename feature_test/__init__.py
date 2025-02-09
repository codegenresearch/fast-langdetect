# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多种语言混合的句子
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))

# 测试单一语言的句子
print(detect("hello world"))
print(detect("你好世界"))
print(detect("こんにちは世界"))
print(detect("안녕하세요 세계"))
print(detect("Bonjour le monde"))
print(detect("Hallo Welt"))
print(detect("Hola mundo"))
print(detect("Ciao mondo"))
print(detect("Привет, мир!"))
print(detect("Bonjour tout le monde"))

# 测试 detect_language 函数
print(detect_language("hello world"))
print(detect_language("你好世界"))
print(detect_language("こんにちは世界"))
print(detect_language("안녕하세요 세계"))
print(detect_language("Bonjour le monde"))
print(detect_language("Hallo Welt"))
print(detect_language("Hola mundo"))
print(detect_language("Ciao mondo"))
print(detect_language("Привет, мир!"))
print(detect_language("Bonjour tout le monde"))
print(detect_language("هذه هي رسالة اختبار"))
print(detect_language("Dies ist ein Testnachricht"))
print(detect_language("Este es un mensaje de prueba"))
print(detect_language("Questa è un messaggio di prova"))
print(detect_language("Это тестовое сообщение"))
print(detect_language("Ce est un message de test"))