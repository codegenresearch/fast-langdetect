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
print(detect_language("これらの機関主辦の課程、多以基本コンピュータ使用為主、例えば文書処理、中文入力、インターネットアプリケーション等"))  # 测试日语, 预期输出: 'JA'
print(detect_language("这些机构主办的课程，多以基本电脑使用为主，例如文書處理、中文输入、互联网应用等"))  # 测试简体中文, 预期输出: 'ZH'
print(detect_language("이러한 기관이 주최하는 과정은 일반적으로 기본 컴퓨터 사용을 중점으로 하며, 예를 들어 문서 처리, 중국어 입력, 인터넷 애플리케이션 등을 다룹니다"))  # 测试韩语, 예상 출력: 'KO'
print(detect_language("Ces institutions organisent des cours axés sur l'utilisation de base de l'informatique, par exemple le traitement de documents, la saisie chinoise, les applications Internet, etc."))  # 테스트 프랑스어, 예상 출력: 'FR'
print(detect_language("Diese Einrichtungen bieten Kurse, die auf die grundlegende Computernutzung abzielen, z. B. Textverarbeitung, Chinesische Eingabe, Internetanwendungen usw."))  # 테스트 독일어, 예상 출력: 'DE'
print(detect_language("Estas instituciones ofrecen cursos centrados en el uso básico de la computadora, por ejemplo, procesamiento de documentos, entrada chinesa, aplicaciones de Internet, etc."))  # 테스트 스페인어, 예상 출력: 'ES'
print(detect_language("Queste istituzioni offrono corsi incentrati sull'uso di base del computer, ad esempio l'elaborazione di documenti, l'inserimento cinese, le applicazioni Internet, ecc."))  # 테스트 이탈리아어, 예상 출력: 'IT'
print(detect_language("Essas instituições oferecem cursos focados no uso básico do computador, por exemplo, processamento de documentos, entrada chinesa, aplicações de internet, etc."))  # 테스트 포르투갈어, 예상 출력: 'PT'
print(detect_language("Bu kurumlar, belge işleme, Çince giriş, İnternet uygulamaları vb. gibi temel bilgisayar kullanımına odaklanan kurslar sunar"))  # 테스트 Türkçe, 예상 출력: 'TR'