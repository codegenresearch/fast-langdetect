# -*- coding: utf-8 -*-

from .ft_detect import detect as detect_language, detect_langs as detect_languages, detect_multilingual as detect_multiple_languages  # noqa: F401

import warnings

warnings.warn("The function 'detect' is deprecated. Use 'detect_language' instead.", DeprecationWarning)
warnings.warn("The function 'detect_langs' is deprecated. Use 'detect_languages' instead.", DeprecationWarning)
warnings.warn("The function 'detect_multilingual' is deprecated. Use 'detect_multiple_languages' instead.", DeprecationWarning)