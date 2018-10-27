# -*- coding: utf-8 -*-

"""Main module."""

import operator
import sys
from sys import stdin
import os
from pathlib import Path
import humanize
import fcntl


def doit():
    """
    Given a list of paths separated by newline, output
    the list of files and their size in bytes sorted by size.
    """

    # make stdin a non-blocking file
    fdescriptor = sys.stdin.fileno()
    flock = fcntl.fcntl(fdescriptor, fcntl.F_GETFL)
    fcntl.fcntl(fdescriptor, fcntl.F_SETFL, flock | os.O_NONBLOCK)

    try:
        std = sys.stdin.readlines()
    except BaseException:
        print('No input')

    flist = {}

    if not stdin.isatty():
        print('fail')
        sys.exit()

    for line in std:
        path = Path(line.strip()).resolve()
        if os.path.exists(path):
            flist[path] = os.stat(path).st_size

    # sort by size
    for path, size in sorted(flist.items(), key=operator.itemgetter(1)):
        print(f'{humanize.naturalsize(size, gnu=True)} {path}')
