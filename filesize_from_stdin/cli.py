# -*- coding: utf-8 -*-

import sys
import click
from .filesize_from_stdin import doit
"""Console script for filesize_from_stdin."""


@click.command()
def main():
    """Console script for filesize_from_stdin."""
    doit()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
