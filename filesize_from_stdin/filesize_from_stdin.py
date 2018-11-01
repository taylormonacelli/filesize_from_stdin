# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
from pathlib import Path
import humanize


def get_file_list(filenames):
    """Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    filenames = list(filenames)

    # prevent blocking if stdin is empty
    if not sys.stdin.isatty():
        filenames += list(sys.stdin)

    dct = {}

    for filename in filenames:
        path = Path(filename.strip())
        if path.exists():
            dct[str(path)] = path.stat().st_size

    return dct


def display_friendly(dct):
    """Print list of files with file's size"""
    # sort by size
    for path, size in sorted(dct.items(), key=operator.itemgetter(1)):
        size = humanize.naturalsize(size, gnu=True)
        print('{} {}'.format(size, path))


if __name__ == "__main__":
    # execute only if run as a script
    display_friendly(get_file_list())
