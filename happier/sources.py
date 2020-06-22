# This code is derived from isort which is Copyright (c) 2013 Timothy
# Edmund Crosley and falls under the MIT licence.  Find it on
# https://github.com/timothycrosley/isort/ My compliments to Timothy
# Crosley et al. for this beautiful code.
import os
import re
import stat
from pathlib import Path
from typing import Iterable, Iterator

shebang_re = re.compile(br"^#!.*\bpython[23w]?\b")

SUPPORTED_EXTENSIONS = (".py", ".pyi", ".pyx")


def is_python_file(path: str) -> bool:
    _root, ext = os.path.splitext(path)
    if ext in SUPPORTED_EXTENSIONS:
        return True
    if ext in (".pex",):
        return False

    # Skip editor backup files.
    if path.endswith("~"):
        return False

    try:
        if stat.S_ISFIFO(os.stat(path).st_mode):
            return False
    except OSError:
        pass

    try:
        with open(path, "rb") as fp:
            line = fp.readline(100)
    except OSError:
        return False
    else:
        return bool(shebang_re.match(line))


def iter_source_code(paths: Iterable[str]) -> Iterator[str]:
    """Iterate over all Python source files defined in paths."""
    for path in paths:
        if os.path.isdir(path):
            for dirpath, dirnames, filenames in os.walk(
                path, topdown=True, followlinks=True
            ):
                Path(dirpath)
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    if is_python_file(filepath):
                        yield filepath
        else:
            yield path
