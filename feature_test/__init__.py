# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

# 测试多种语言混合的句子，预期输出为包含语言代码和分数的字典列表
print("Testing multilingual detection:")
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))
# 预期输出示例: [{'lang': 'en', 'score': 0.9}, {'lang': 'zh', 'score': 0.8}, {'lang': 'ru', 'score': 0.7}]

# 测试单一语言的句子
print("\nTesting single language detection:")
print("English:", detect("hello world"))
print("Simplified Chinese:", detect("你好世界"))
print("Japanese:", detect("こんにちは世界"))
print("Korean:", detect("안녕하세요 세계"))
print("French:", detect("Bonjour le monde"))
print("German:", detect("Hallo Welt"))
print("Spanish:", detect("Hola mundo"))
print("Italian:", detect("Ciao mondo"))
print("Russian:", detect("Привет, мир!"))
print("Traditional Chinese:", detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# 测试 detect_language 函数，预期输出为大写的语言代码
print("\nTesting detect_language function:")
print("English:", detect_language("hello world"))
print("Simplified Chinese:", detect_language("你好世界"))
print("Japanese:", detect_language("こんにちは世界"))
print("Korean:", detect_language("안녕하세요 세계"))
print("French:", detect_language("Bonjour le monde"))
print("German:", detect_language("Hallo Welt"))
print("Spanish:", detect_language("Hola mundo"))
print("Italian:", detect_language("Ciao mondo"))
print("Russian:", detect_language("Привет, мир!"))
print("Traditional Chinese:", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
print("Arabic:", detect_language("هذه هي رسالة اختبار"))
print("Dutch:", detect_language("Dit is een testbericht"))
print("Portuguese:", detect_language("Esta é uma mensagem de teste"))
print("Polish:", detect_language("To jest wiadomość testowa"))
print("Ukrainian:", detect_language("Це тестове повідомлення"))
print("Turkish:", detect_language("Bu bir test mesajıdır"))