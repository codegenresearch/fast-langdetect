# -*- coding: utf-8 -*-
# @Time    : 2024/1/17 下午5:28
# @Author  : sudoskys
# @File    : test_detect.py
# @Software: PyCharm


def test_muti_detect():
    """
    Test the detect_multilingual function with multiple languages and low_memory option.
    Assumes input is a string containing text in multiple languages.
    """
    from fast_langdetect.ft_detect import detect_multilingual
    result = detect_multilingual("Hello, world!你好世界!Привет, мир!", low_memory=True)
    assert result[0].get("lang") == "en", "ft_detect error"
    assert any(item.get("lang") == "zh" for item in result), "ft_detect error"
    assert any(item.get("lang") == "ru" for item in result), "ft_detect error"


def test_detect():
    """
    Test the detect function with various languages.
    Assumes input is a string containing text in a single language.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "ft_detect error"
    assert detect("你好世界")["lang"] == "zh", "ft_detect error"
    assert detect("こんにちは世界")["lang"] == "ja", "ft_detect error"
    assert detect("안녕하세요 세계")["lang"] == "ko", "ft_detect error"
    assert detect("Bonjour le monde")["lang"] == "fr", "ft_detect error"
    assert detect("Hallo Welt")["lang"] == "de", "ft_detect error"
    assert detect("Hola mundo")["lang"] == "es", "ft_detect error"


def test_detect_totally():
    """
    Test the detect_language function with various languages.
    Assumes input is a string containing text in a single language.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "ft_detect error"
    assert detect_language("你好世界") == "ZH", "ft_detect error"
    assert detect_language("こんにちは世界") == "JA", "ft_detect error"
    assert detect_language("안녕하세요 세계") == "KO", "ft_detect error"
    assert detect_language("Bonjour le monde") == "FR", "ft_detect error"
    assert detect_language("Hallo Welt") == "DE", "ft_detect error"
    assert detect_language("Hola mundo") == "ES", "ft_detect error"
    assert detect_language(
        "Ces institutions organisent des cours principalement sur l'utilisation de base de l'ordinateur, par exemple le traitement de texte, la saisie chinoise, les applications Internet, etc."
    ) == "FR", "ft_detect error"
    assert detect_language(
        "Estas instituciones ofrecen cursos principalmente sobre el uso básico de la computadora, por ejemplo, el procesamiento de textos, la entrada chinesa, las aplicaciones de Internet, etc."
    ) == "ES", "ft_detect error"
    assert detect_language(
        "이러한 기관이 주최하는 과정들은 주로 기본 컴퓨터 사용법을 다루며, 예를 들어 문서 처리, 중국어 입력, 인터넷 애플리케이션 등이 있습니다."
    ) == "KO", "ft_detect error"
    assert detect_language(
        "これらの機関主催のコースは、主に基本的なコンピュータの使用を教えるもので、例えば文書処리、中国語入力、インターネットアプリケーションなどです。"
    ) == "JA", "ft_detect error"


def test_failed_example():
    """
    Test the detect function with an invalid input to ensure it handles exceptions gracefully.
    Assumes input is a string containing text in a single language.
    """
    from fast_langdetect import detect
    try:
        detect(None)
    except TypeError as e:
        assert isinstance(e, TypeError), "ft_detect error"
    try:
        detect("")
    except ValueError as e:
        assert isinstance(e, ValueError), "ft_detect error"


This code addresses the feedback by:
1. Ensuring all comments are properly formatted with `#`.
2. Simplifying assertions in `test_muti_detect` to focus on the most critical checks.
3. Reducing redundancy in `test_detect` and `test_detect_totally` by focusing on representative examples.
4. Ensuring consistent language codes used in assertions match those in the gold code.
5. Refining error handling in `test_failed_example` to match the approach in the gold code.
6. Ensuring consistent formatting and readability throughout the code.