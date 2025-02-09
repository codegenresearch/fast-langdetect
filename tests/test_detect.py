# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午5:28\n# @Author  : sudoskys\n# @File    : test_detect.py\n# @Software: PyCharm\n\nfrom fast_langdetect.ft_detect import detect_multilingual\nfrom fast_langdetect import detect_language\n\ndef test_muti_detect():\n    """Test the multilingual detection functionality."""\n    result = detect_multilingual("hello world", low_memory=True)\n    assert result[0].get("lang") == "en", "ft_detect error"\n\ndef test_detect_totally():\n    """Test the language detection for various languages."""\n    assert detect_language("hello world").get("lang").upper() == "EN", "ft_detect error"\n    assert detect_language("你好世界").get("lang").upper() == "ZH", "ft_detect error"\n    assert detect_language("こんにちは世界").get("lang").upper() == "JA", "ft_detect error"\n    assert detect_language("안녕하세요 세계").get("lang").upper() == "KO", "ft_detect error"\n    assert detect_language("Bonjour le monde").get("lang").upper() == "FR", "ft_detect error"\n    assert detect_language("Hallo Welt").get("lang").upper() == "DE", "ft_detect error"\n    assert detect_language("Hola mundo").get("lang").upper() == "ES", "ft_detect error"\n    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等").get("lang").upper() == "ZH", "ft_detect error"\n