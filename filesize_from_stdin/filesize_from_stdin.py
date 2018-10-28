# -*- coding: utf-8 -*-

"""Main module."""
import operator
import sys
from pathlib import Path
import humanize


def doit():
    """
    Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    flist = {}

    if sys.stdin.isatty():
        print('fail')
        sys.exit(1)

    for line in sys.stdin.readlines():
        path = Path(line.strip())
        if path.exists():
            flist[str(path.resolve())] = path.stat().st_size

    # sort by size
    for path, size in sorted(flist.items(), key=operator.itemgetter(1)):
        print(("%s %s" % (humanize.naturalsize(size, gnu=True), path)))
