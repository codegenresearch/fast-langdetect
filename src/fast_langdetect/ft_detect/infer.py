# -*- coding: utf-8 -*-\n# @Time    : 2024/1/17 下午8:30\n# @Author  : sudoskys\n# @File    : infer.py\n# @Software: PyCharm\nimport logging\nimport os\nfrom pathlib import Path\nfrom typing import Dict, Union, List\nimport fasttext\nfrom robust_downloader import download\nlogger = logging.getLogger(__name__)\nMODELS = {"low_mem": None, "high_mem": None}\nFTLANG_CACHE = os.getenv("FTLANG_CACHE", "/tmp/fasttext-langdetect")\nclass DetectError(Exception):\n    """Custom exception for detection errors."""\n    pass\ndef get_model_map(low_memory=False):\n    """\n    Get the model map based on memory preference.\n    :param low_memory: Boolean indicating whether to use the low memory model.\n    :return: Tuple containing mode, cache path, model name, and download URL.\n    """\n    if low_memory:\n        return "low_mem", FTLANG_CACHE, "lid.176.ftz", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.ftz"\n    else:\n        return "high_mem", FTLANG_CACHE, "lid.176.bin", "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin"\ndef get_model_loaded(low_memory=False, download_proxy=None):\n    """\n    Load the appropriate model based on memory preference.\n    :param low_memory: Boolean indicating whether to use the low memory model.\n    :param download_proxy: Proxy for downloading the model.\n    :return: Loaded fastText model.\n    :raises Exception: If there is an error loading or downloading the model.\