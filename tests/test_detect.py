# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午5:28\n# @Author  : sudoskys\n# @File    : test_detect.py\n# @Software: PyCharm\nimport warnings\nfrom fast_langdetect import detect_multiple_languages, detect_language\n\ndef test_detect_multiple_languages():\n    warnings.warn('test_muti_detect is deprecated, use test_detect_multiple_languages instead.', DeprecationWarning)\n    result = detect_multiple_languages("hello world", low_memory=True)\n    assert result[0].get("lang") == "en", "ft_detect error"\n\ndef test_identify_languages():\n    warnings.warn('test_detect_totally is deprecated, use test_identify_languages instead.', DeprecationWarning)\n    assert detect_language("hello world").upper() == "EN", "ft_detect error"\n    assert detect_language("你好世界").upper() == "ZH", "ft_detect error"\n    assert detect_language("こんにちは世界").upper() == "JA", "ft_detect error"\n