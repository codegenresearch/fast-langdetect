# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午5:28\n# @Author  : sudoskys\n# @File    : test_detect.py\n# @Software: PyCharm\n\ndef test_multilingual_detection():\n    """Test the multilingual detection functionality."""\n    from fast_langdetect import detect_multilingual    \\n    result = detect_multilingual("hello world", low_memory=True)\n    assert result[0].get("lang") == "en", "Multilingual detection error"\n\ndef test_language_detection_english():\n    """Test the language detection for English."""\n    from fast_langdetect import detect_languages    \\)n    result = detect_languages("hello world")\n    assert result[0].lang == "en", "Language detection error for English"\n\ndef test_language_detection_chinese():\n    """Test the language detection for Chinese."""\n    from fast_langdetect import detect_languages    \\)n    result = detect_languages("你好世界")\n    assert result[0].lang == "zh", "Language detection error for Chinese"\n\ndef test_language_detection_japanese():\n    """Test the language detection for Japanese."""\n    from fast_langdetect import detect_languages    \\)n    result = detect_languages("こんにちは世界")\n    assert result[0].lang == "ja", "Language detection error for Japanese"\n