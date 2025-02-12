# -*- coding: utf-8 -*-

import warnings
from .ft_detect import detect as deprecated_detect, detect_langs as deprecated_detect_langs, detect_multilingual as deprecated_detect_multilingual  # noqa: F401

warnings.warn("The functions detect, detect_langs, and detect_multilingual are deprecated. Use detect_text, detect_languages, and detect_multilingual_text instead.", DeprecationWarning)

from .ft_detect import detect_text, detect_languages, detect_multilingual_text