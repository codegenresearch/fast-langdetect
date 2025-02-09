# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys
# @File    : __init__.py.py
# @Software: PyCharm
from fast_langdetect import detect, detect_multilingual, detect_language

# 测试 detect_multilingual 函数
# 预期输出: [{'lang': 'en', 'score': ...}, {'lang': 'zh', 'score': ...}, {'lang': 'ru', 'score': ...}]
print(detect_multilingual("Hello, world!你好世界!Привет, мир!"))  # 测试混合语言: 英语, 简体中文, 俄语

# 测试 detect 函数
print(detect("hello world"))  # 测试英语, 预期输出: 'en'
print(detect("Привет, мир!"))  # 测试俄语, 预期输出: 'ru'
print(detect("こんにちは世界"))  # 测试日语, 预期输出: 'ja'
print(detect("안녕하세요 세계"))  # 测试韩语, 预期输出: 'ko'
print(detect("Bonjour le monde"))  # 测试法语, 预期输出: 'fr'
print(detect("Hallo Welt"))  # 测试德语, 预期输出: 'de'
print(detect("Hola mundo"))  # 测试西班牙语, 预期输出: 'es'
print(detect("Ciao mondo"))  # 测试意大利语, 预期输出: 'it'
print(detect("Olá mundo"))  # 测试葡萄牙语, 预期输出: 'pt'
print(detect("Merhaba dünya"))  # 测试土耳其语, 预期输出: 'tr'
print(detect("你好，世界！Hello, world！Привет, мир！"))  # 测试混合语言: 简体中文, 英语, 俄语

# 测试 detect_language 函数
print(detect_language("hello world"))  # 测试英语, 预期输出: 'EN'
print(detect_language("你好世界"))  # 测试简体中文, 预期输出: 'ZH'
print(detect_language("こんにちは世界"))  # 测试日语, 预期输出: 'JA'
print(detect_language("안녕하세요 세계"))  # 测试韩语, 预期输出: 'KO'
print(detect_language("Bonjour le monde"))  # 测试法语, 预期输出: 'FR'
print(detect_language("Hallo Welt"))  # 测试德语, 预期输出: 'DE'
print(detect_language("Hola mundo"))  # 测试西班牙语, 预期输出: 'ES'
print(detect_language("Ciao mondo"))  # 测试意大利语, 预期输出: 'IT'
print(detect_language("Olá mundo"))  # 测试葡萄牙语, 预期输出: 'PT'
print(detect_language("Merhaba dünya"))  # 测试土耳其语, 预期输出: 'TR'
print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # 测试繁体中文, 预期输出: 'ZH'