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
    assert any(item.get("lang") == "en" for item in result), "English detection failed"
    assert any(item.get("lang") == "zh" for item in result), "Chinese detection failed"
    assert any(item.get("lang") == "ru" for item in result), "Russian detection failed"


def test_detect():
    """
    Test the detect function with various languages.
    Assumes input is a string containing text in a single language.
    """
    from fast_langdetect import detect
    assert detect("hello world")["lang"] == "en", "English detection failed"
    assert detect("你好世界")["lang"] == "zh", "Chinese detection failed"
    assert detect("こんにちは世界")["lang"] == "ja", "Japanese detection failed"
    assert detect("안녕하세요 세계")["lang"] == "ko", "Korean detection failed"
    assert detect("Bonjour le monde")["lang"] == "fr", "French detection failed"
    assert detect("Hallo Welt")["lang"] == "de", "German detection failed"
    assert detect("Hola mundo")["lang"] == "es", "Spanish detection failed"
    assert detect("Ces institutions organisent des cours principalement sur l'utilisation de base de l'ordinateur, par exemple le traitement de texte, la saisie chinoise, les applications Internet, etc.")["lang"] == "fr", "French detection failed"
    assert detect("Estas instituciones ofrecen cursos principalmente sobre el uso básico de la computadora, por ejemplo, el procesamiento de textos, la entrada chinesa, las aplicaciones de Internet, etc.")["lang"] == "es", "Spanish detection failed"
    assert detect("이러한 기관이 주최하는 과정들은 주로 기본 컴퓨터 사용법을 다루며, 예를 들어 문서 처리, 중국어 입력, 인터넷 애플리케이션 등이 있습니다.")["lang"] == "ko", "Korean detection failed"


def test_detect_totally():
    """
    Test the detect_language function with various languages.
    Assumes input is a string containing text in a single language.
    """
    from fast_langdetect import detect_language
    assert detect_language("hello world") == "EN", "English detection failed"
    assert detect_language("你好世界") == "ZH", "Chinese detection failed"
    assert detect_language("こんにちは世界") == "JA", "Japanese detection failed"
    assert detect_language("안녕하세요 세계") == "KO", "Korean detection failed"
    assert detect_language("Bonjour le monde") == "FR", "French detection failed"
    assert detect_language("Hallo Welt") == "DE", "German detection failed"
    assert detect_language("Hola mundo") == "ES", "Spanish detection failed"
    assert detect_language("Ces institutions organisent des cours principalement sur l'utilisation de base de l'ordinateur, par exemple le traitement de texte, la saisie chinoise, les applications Internet, etc.") == "FR", "French detection failed"
    assert detect_language("Estas instituciones ofrecen cursos principalmente sobre el uso básico de la computadora, por ejemplo, el procesamiento de textos, la entrada chinesa, las aplicaciones de Internet, etc.") == "ES", "Spanish detection failed"
    assert detect_language("이러한 기관이 주최하는 과정들은 주로 기본 컴퓨터 사용법을 다루며, 예를 들어 문서 처리, 중국어 입력, 인터넷 애플리케이션 등이 있습니다.") == "KO", "Korean detection failed"
    assert detect_language("これらの機関主催のコースは、主に基本的なコンピュータの使用を教えるもので、例えば文書処理、中国語入力、インターネットアプリケーションなどです。") == "JA", "Japanese detection failed"
    assert detect_language("これらの機関が主催するコースは、主に基本的なコンピュータの使用を教えるもので、例えば文書処리、中国語入力、インターネットアプリケーションなどです。") == "JA", "Japanese detection failed"
    assert detect_language("これらの機関が主催するコースは、主に基本的なコンピュータの使用을 다루며、例えば文서 처리、중국어 입력, 인터넷 애플리케이션 등이 있습니다.") == "JA", "Japanese detection failed"