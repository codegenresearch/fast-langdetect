# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm

import logging
from fast_langdetect import detect_multilingual, detect_languages

# Setting up logging for deprecated functionality
logging.basicConfig(level=logging.WARNING)
logger = logging.getLogger(__name__)

def test_multilingual_detection():
    """
    Tests the multilingual detection functionality.
    """
    result = detect_multilingual("hello world", low_memory=True)
    assert result[0].get("lang") == "en", "Multilingual detection error"

def test_language_detection():
    """
    Tests the language detection functionality.
    """
    assert detect_languages("hello world")[0].lang == "en", "Language detection error"
    assert detect_languages("你好世界")[0].lang == "zh", "Language detection error"
    assert detect_languages("こんにちは世界")[0].lang == "ja", "Language detection error"

# Deprecation warning for old function names
logger.warning("The function 'detect_langs' is deprecated. Use 'detect_languages' instead.")