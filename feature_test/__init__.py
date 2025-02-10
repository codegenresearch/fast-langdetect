# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_multilingual_detection():
    """
    Tests the multilingual detection function with a mixed-language string.
    The function should return a list of detected languages with their scores.
    This test checks if the function can handle multiple languages in a single string.
    """
    # Test with low_memory=True
    result_low_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    print("Multilingual detection with low_memory=True:", result_low_memory)
    
    # Test with low_memory=False
    result_high_memory = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    print("Multilingual detection with low_memory=False:", result_high_memory)

def test_single_language_detection():
    """
    Tests the single language detection function with various strings.
    The function should return the detected language code.
    This test checks if the function can accurately detect the language of single-language strings.
    """
    print("Single language detection for 'hello world':", detect("hello world"))
    print("Single language detection for 'Привет, мир!':", detect("Привет, мир!"))
    print("Single language detection for '你好世界':", detect("你好世界"))
    print("Single language detection for 'こんにちは世界':", detect("こんにちは世界"))
    print("Single language detection for '안녕하세요 세계':", detect("안녕하세요 세계"))
    print("Single language detection for 'Bonjour le monde':", detect("Bonjour le monde"))
    print("Single language detection for 'Hallo Welt':", detect("Hallo Welt"))
    print("Single language detection for 'Hola mundo':", detect("Hola mundo"))
    print("Single language detection for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

def test_language_detection():
    """
    Tests the language detection function with various strings.
    The function should return the detected language code in uppercase.
    This test checks if the function can accurately detect the language of single-language strings.
    """
    print("Language detection for 'Привет, мир!':", detect_language("Привет, мир!"))
    print("Language detection for '你好世界':", detect_language("你好世界"))
    print("Language detection for 'こんにちは世界':", detect_language("こんにちは世界"))
    print("Language detection for '안녕하세요 세계':", detect_language("안녕하세요 세계"))
    print("Language detection for 'Bonjour le monde':", detect_language("Bonjour le monde"))
    print("Language detection for 'Hallo Welt':", detect_language("Hallo Welt"))
    print("Language detection for 'Hola mundo':", detect_language("Hola mundo"))
    print("Language detection for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))

# Run the tests
test_multilingual_detection()
test_single_language_detection()
test_language_detection()