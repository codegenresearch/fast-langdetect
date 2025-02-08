# -*- coding: utf-8 -*-\n# @Time    : 2024/1/18 上午11:41\n# @Author  : sudoskys\nfrom fast_langdetect import detect, detect_multilingual, detect_language\n\n# Test detect_multilingual with a mix of English, Chinese, Russian, and Japanese\n# This test checks the ability to detect multiple languages in a single string\nprint(detect_multilingual("Hello, world! 你好世界! Привет, мир! こんにちは世界!"))\n# Test detect_multilingual with low_memory=True and a mix of English, Chinese, Russian, and Japanese\nprint(detect_multilingual("Hello, world! 你好世界! Привет, мир! こんにちは世界!", low_memory=True))\n\n# Test detect with various languages to ensure each is correctly identified\n# English\nprint(detect("hello world"))\n# Chinese (Simplified)\nprint(detect("你好世界"))\n# Russian\nprint(detect("Привет, мир!"))\n# Japanese\nprint(detect("こんにちは世界"))\n# Korean\nprint(detect("안녕하세요 세계"))\n# French\nprint(detect("Bonjour le monde"))\n# German\nprint(detect("Hallo Welt"))\n# Spanish\nprint(detect("Hola mundo"))\n# Chinese (Traditional)\nprint(detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))\n\n# Test detect_language with various languages to ensure each is correctly identified and returns the language code\n# English\nprint(detect_language("hello world"))\n# Chinese (Simplified)\nprint(detect_language("你好世界"))\n# Russian\nprint(detect_language("Привет, мир!"))\n# Japanese\nprint(detect_language("こんにちは世界"))\n# Korean\nprint(detect_language("안녕하세요 세계"))\n# French\nprint(detect_language("Bonjour le monde"))\n# German\nprint(detect_language("Hallo Welt"))\n# Spanish\nprint(detect_language("Hola mundo"))\n# Chinese (Traditional)\nprint(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))\n