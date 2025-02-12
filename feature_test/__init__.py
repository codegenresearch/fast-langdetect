# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language


def test_multilingual_detection():
    """\n    Test the detect_multilingual function with a mixed language string.\n    Expected to return a list of detected languages with their scores.\n    """
    text = "Hello, world!你好世界!Привет, мир!"
    result = detect_multilingual(text, low_memory=True)
    print(result)


def test_single_language_detection():
    """\n    Test the detect function with various single language strings.\n    Expected to return the detected language code.\n    """
    try:
        print(detect("hello world"))  # Expected: en
        print(detect("Привет, мир!"))  # Expected: uk
        print(detect("你好世界"))  # Expected: zh
        print(detect("こんにちは世界"))  # Expected: ja
        print(detect("안녕하세요 세계"))  # Expected: ko
        print(detect("Bonjour le monde"))  # Expected: fr
        print(detect("Hallo Welt"))  # Expected: de
        print(detect("Hola mundo"))  # Expected: es
    except Exception as e:
        print(f"An error occurred: {e}")


def test_language_detection():
    """\n    Test the detect_language function with various single language strings.\n    Expected to return the detected language code in uppercase.\n    """
    try:
        print(detect_language("Привет, мир!"))  # Expected: UK
        print(detect_language("你好世界"))  # Expected: ZH
        print(detect_language("こんにちは世界"))  # Expected: JA
        print(detect_language("안녕하세요 세계"))  # Expected: KO
        print(detect_language("Bonjour le monde"))  # Expected: FR
        print(detect_language("Hallo Welt"))  # Expected: DE
        print(detect_language("Hola mundo"))  # Expected: ES
        print(detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))  # Expected: ZH
    except Exception as e:
        print(f"An error occurred: {e}")


# Run the tests
test_multilingual_detection()
test_single_language_detection()
test_language_detection()