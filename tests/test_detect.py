# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午5:28\n# @Author  : sudoskys\n# @File    : test_detect.py\n# @Software: PyCharm\nfrom fast_langdetect import detect_multiple_languages, detect_language\ndef test_detect_multiple_languages_with_low_memory():\n    result = detect_multiple_languages("hello world", low_memory=True)\n    assert result[0].get("lang") == "en", "ft_detect error"\ndef test_detect_language_hello_world():\n    assert detect_language("hello world").upper() == "EN", "ft_detect error"\ndef test_detect_language_chinese():\n    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"\ndef test_detect_language_japanese():\n    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"\ndef test_detect_language_korean():\n    assert detect_language("안녕하세요 세계").upper() == "KO", "ft_detect error"\ndef test_detect_language_french():\n    assert detect_language("Bonjour le monde").upper() == "FR", "ft_detect error"\ndef test_detect_language_german():\n    assert detect_language("Hallo Welt").upper() == "DE", "ft_detect error"\ndef test_detect_language_spanish():\n    assert detect_language("Hola mundo").upper() == "ES", "ft_detect error"\ndef test_detect_language_chinese_traditional():\n    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").upper() == "ZH", "ft_detect error"\