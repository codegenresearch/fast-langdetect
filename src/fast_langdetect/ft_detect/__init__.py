# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午4:00\n# @Author  : sudoskys\n# @File    : __init__.py\nfrom fast_langdetect import detect, detect_multilingual, detect_language  # Ensure correct imports\nimport logging\n\n# Setting up logging"logging.basicConfig(level=logging.INFO)\n\ndef contains_japanese(text):\n    """Check if the text contains Japanese characters.":param text: str - The text to check.":return: bool - True if Japanese characters are present, False otherwise."""\n    for ch in text:\n        if 0x3040 <= ord(ch) <= 0x30FF or 0x4E00 <= ord(ch) <= 0x9FFF:\n            return True\n    return False\n\ndef detect_language_code(sentence, *, low_memory: bool = True):\n    """Detect the language of the given sentence.":param sentence: str - The sentence to detect the language of.":param low_memory: bool - Whether to use low memory mode (default: True).":return: str - Language code in uppercase (e.g., ZH, EN, JA, KO, FR, DE, ES)."""\n    try:\n        lang_code = detect(sentence, low_memory=low_memory).get("lang").upper()\n        if lang_code == "JA" and not contains_japanese(sentence):\n            logging.warning("Detected language is Japanese but no Japanese characters found. Assuming Chinese.")\n            lang_code = "ZH"\n        return lang_code\n    except Exception as e:\n        logging.error(f"Error detecting language: {e}")\n        raise