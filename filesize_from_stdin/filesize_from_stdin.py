# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
import os
from pathlib import Path
import humanize


def doit():
    """test stuff"""

    flist = {}

    if sys.stdin.isatty():
        print('fail')
        sys.exit()

    for line in sys.stdin.readlines():
        path = Path(line.strip()).resolve()
        if os.path.exists(path):
            flist[path] = os.stat(path).st_size

    # sort by size
    for path, size in sorted(flist.items(), key=operator.itemgetter(1)):
        print(f'{humanize.naturalsize(size, gnu=True)} {path}')
