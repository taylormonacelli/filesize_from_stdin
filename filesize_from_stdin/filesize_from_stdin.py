# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
from pathlib import Path
import humanize


def get_file_list_from_stdin(stdin):
    """
    Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    if sys.stdin.isatty():
        sys.stderr.write('fail')
        sys.exit(1)

    dct = {}

    for line in stdin:
        path = Path(line.strip())
        if path.exists():
            dct[str(path.resolve())] = path.stat().st_size

    return dct


def display_friendly(dct):
    """
    Print list of files with file's size
    """
    # sort by size
    for path, size in sorted(dct.items(), key=operator.itemgetter(1)):
        print("%s %s" % (humanize.naturalsize(size, gnu=True), path))


if __name__ == "__main__":
    # execute only if run as a script
    display_friendly(get_file_list_from_stdin(sys.stdin))
