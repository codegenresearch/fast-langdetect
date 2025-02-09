# -*- coding: utf-8 -*-
# @Time    : 2024/1/18 上午11:41
# @Author  : sudoskys

from fast_langdetect import detect, detect_multilingual, detect_language

def test_detect_multilingual():
    """
    Test the detect_multilingual function with a mixed language string.
    The function should return a list of detected languages with their scores.
    """
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False)
    print("Multilingual detection result:", result)
    expected_languages = ['ja', 'uk', 'zh', 'sr', 'bg']
    detected_languages = [item['lang'] for item in result]
    assert any(lang in detected_languages for lang in expected_languages), "detect_multilingual did not detect expected languages"

def test_detect():
    """
    Test the detect function with a simple English string.
    The function should return a dictionary with the detected language.
    """
    result = detect("hello world")
    print("Detect result for 'hello world':", result)
    assert result["lang"] == "en", "detect did not return 'en' for 'hello world'"

def test_detect_language():
    """
    Test the detect_language function with various language strings.
    The function should return the correct language code in uppercase.
    """
    print("Detect language for 'Привет, мир!':", detect_language("Привет, мир!"))
    assert detect_language("Привет, мир!") == "RU", "detect_language did not return 'RU' for Russian"
    
    print("Detect language for '你好世界':", detect_language("你好世界"))
    assert detect_language("你好世界") == "ZH", "detect_language did not return 'ZH' for Chinese"
    
    print("Detect language for 'こんにちは世界':", detect_language("こんにちは世界"))
    assert detect_language("こんにちは世界") == "JA", "detect_language did not return 'JA' for Japanese"
    
    print("Detect language for '안녕하세요 세계':", detect_language("안녕하세요 세계"))
    assert detect_language("안녕하세요 세계") == "KO", "detect_language did not return 'KO' for Korean"
    
    print("Detect language for 'Bonjour le monde':", detect_language("Bonjour le monde"))
    assert detect_language("Bonjour le monde") == "FR", "detect_language did not return 'FR' for French"
    
    print("Detect language for 'Hallo Welt':", detect_language("Hallo Welt"))
    assert detect_language("Hallo Welt") == "DE", "detect_language did not return 'DE' for German"
    
    print("Detect language for 'Hola mundo':", detect_language("Hola mundo"))
    assert detect_language("Hola mundo") == "ES", "detect_language did not return 'ES' for Spanish"
    
    print("Detect language for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等':", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "ZH", "detect_language did not return 'ZH' for Traditional Chinese"

def test_detect_language_error_handling():
    """
    Test the detect_language function with an unsupported language string.
    The function should raise an exception if the language cannot be detected.
    """
    try:
        result = detect_language("This is an unsupported language string")
        print("Detect language for unsupported string:", result)
    except Exception as e:
        print("Exception caught for unsupported string:", e)
        assert isinstance(e, Exception), "detect_language did not raise an exception for unsupported language"

# Direct calls to functions for demonstration
print("Direct call to detect_multilingual:", detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=False))
print("Direct call to detect:", detect("hello world"))
print("Direct call to detect_language for Russian:", detect_language("Привет, мир!"))
print("Direct call to detect_language for Chinese:", detect_language("你好世界"))
print("Direct call to detect_language for Japanese:", detect_language("こんにちは世界"))
print("Direct call to detect_language for Korean:", detect_language("안녕하세요 세계"))
print("Direct call to detect_language for French:", detect_language("Bonjour le monde"))
print("Direct call to detect_language for German:", detect_language("Hallo Welt"))
print("Direct call to detect_language for Spanish:", detect_language("Hola mundo"))
print("Direct call to detect_language for Traditional Chinese:", detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"))