# -*- coding: utf-8 -*-

from .ft_detect import detect, detect_multilingual

# Deprecation warning for detect_langs
import warnings
warnings.warn("The function 'detect_langs' is deprecated and will be removed in future versions.", DeprecationWarning)