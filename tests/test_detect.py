# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

import logging
from fast_langdetect import detect_multilingual, detect_language

# Setting up logging for deprecated functionality
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def test_multilingual():
    """
    Tests the multilingual detection functionality.
    """
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Multilingual detection failed for 'hello world'"

def test_single_language():
    """
    Tests the single language detection functionality.
    """
    assert detect_language("hello world") == "en", "Single language detection failed for 'hello world'"
    assert detect_language("你好世界") == "zh", "Single language detection failed for '你好世界'"
    assert detect_language("こんにちは世界") == "ja", "Single language detection failed for 'こんにちは世界'"
    assert detect_language("안녕하세요 세계") == "ko", "Single language detection failed for '안녕하세요 세계'"
    assert detect_language("Bonjour le monde") == "fr", "Single language detection failed for 'Bonjour le monde'"
    assert detect_language("Hallo Welt") == "de", "Single language detection failed for 'Hallo Welt'"
    assert detect_language("Hola mundo") == "es", "Single language detection failed for 'Hola mundo'"
    assert detect_language("這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等") == "zh", "Single language detection failed for '這些機構主辦的課程，多以基本電腦使用為主，例如文書處理、中文輸入、互聯網應用等'"

# Deprecation warning for old function names
logger.warning("The function 'detect_langs' is deprecated. Use 'detect_language' instead.")