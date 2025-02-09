# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_detect_multilingual():
    """
    Test the detect_multilingual function with a mixed language string.
    """
    try:
        result = detect_multilingual("Hello, world!你好世界!Привет, мир!")
        print(result)
        # Expected output: [{'lang': 'ja', 'score': ...}, {'lang': 'uk', 'score': ...}, {'lang': 'zh', 'score': ...}, ...]
    except Exception as e:
        print(f"An error occurred: {e}")

def test_detect():
    """
    Test the detect function with various single language strings.
    """
    try:
        print(detect("hello world"))  # Expected output: 'en'
    except Exception as e:
        print(f"An error occurred: {e}")

def test_detect_language():
    """
    Test the detect_language function with various single language strings.
    """
    try:
        print(detect_language("Привет, мир!"))  # Expected output: 'RU'
        print(detect_language("你好世界"))      # Expected output: 'ZH'
        print(detect_language("こんにちは世界")) # Expected output: 'JA'
        print(detect_language("안녕하세요 세계")) # Expected output: 'KO'
        print(detect_language("Bonjour le monde")) # Expected output: 'FR'
        print(detect_language("Hallo Welt"))     # Expected output: 'DE'
        print(detect_language("Hola mundo"))     # Expected output: 'ES'
        print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等")) # Expected output: 'ZH'
    except Exception as e:
        print(f"An error occurred: {e}")

# Run tests
test_detect_multilingual()
test_detect()
test_detect_language()