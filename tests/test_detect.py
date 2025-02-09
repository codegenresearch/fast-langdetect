# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

def test_muti_detect():
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Language detection failed for 'hello world'"

def test_detect():
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "Language detection failed for 'hello world'"
    assert detect("你好世界")["lang"] == "zh", "Language detection failed for '你好世界'"
    assert detect("こんにちは世界")["lang"] == "ja", "Language detection failed for 'こんにちは世界'"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Language detection failed for '안녕하세요 세계'"
    assert detect("Bonjour le monde")["lang"] == "fr", "Language detection failed for 'Bonjour le monde'"
    assert detect("Hallo Welt")["lang"] == "de", "Language detection failed for 'Hallo Welt'"
    assert detect("Hola mundo")["lang"] == "es", "Language detection failed for 'Hola mundo'"

def test_detect_totally():
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "Language detection failed for 'hello world'"
    assert detect_language("你好世界") == "ZH", "Language detection failed for '你好世界'"
    assert detect_language("こんにちは世界") == "JA", "Language detection failed for 'こんにちは世界'"
    assert detect_language("안녕하세요 세계") == "KO", "Language detection failed for '안녕하세요 세계'"
    assert detect_language("Bonjour le monde") == "FR", "Language detection failed for 'Bonjour le monde'"
    assert detect_language("Hallo Welt") == "DE", "Language detection failed for 'Hallo Welt'"
    assert detect_language("Hola mundo") == "ES", "Language detection failed for 'Hola mundo'"
    assert detect_language(
        "這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等"
    ) == "ZH", "Language detection failed for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等'"

def test_failed_example():
    from fast_langdetect import detect
    try:
        detect("\n")
    except Exception as e:
        assert isinstance(e, Exception), "No language detected for empty input"
    else:
        assert False, "No exception raised for empty input"