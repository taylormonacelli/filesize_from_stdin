# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
from pathlib import Path
import humanize


def file_sizes_from_stdin():
    """
    Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    flist = {}

    if sys.stdin.isatty():
        sys.stderr.write('fail')
        sys.exit(1)

    for line in sys.stdin.readlines():
        path = Path(line.strip())
        if path.exists():
            flist[str(path.resolve())] = path.stat().st_size

    return flist


def display_friendly(lst):
    """Print list of files with file's size"""
    # sort by size
    for path, size in sorted(lst.items(), key=operator.itemgetter(1)):
        print("%s %s" % (humanize.naturalsize(size, gnu=True), path))


if __name__ == "__main__":
    # execute only if run as a script
    display_friendly(file_sizes_from_stdin())
