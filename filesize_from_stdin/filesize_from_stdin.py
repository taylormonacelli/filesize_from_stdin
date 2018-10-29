# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
import io
from pathlib import Path
import humanize


def get_file_list(source=sys.stdin):
    """Get list of files form stdin"""
    lst = []

    if isinstance(source, io.TextIOWrapper):
        # if stdin is empty
        if source.isatty():
            return lst

    for line in source:
        path = Path(line.strip())
        if path.exists():
            lst.append(path.resolve())

    return lst


def get_file_sizes(lst):
    """
    Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    dct = {}

    lst = get_file_list()
    for path in lst:
        dct[str(path)] = path.stat().st_size

    return dct


def display_friendly(dct):
    """Print list of files with file's size"""
    # sort by size
    for path, size in sorted(dct.items(), key=operator.itemgetter(1)):
        print("%s %s" % (humanize.naturalsize(size, gnu=True), path))


if __name__ == "__main__":
    # execute only if run as a script
    display_friendly(get_file_list())
