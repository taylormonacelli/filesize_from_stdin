# -*- coding: utf-8 -*-
from .filesize_from_stdin import doit
"""Console script for filesize_from_stdin."""

import click
import sys
import os

sys.path.insert(0,
                os.path.join(
                    os.path.dirname(__file__),
                    '..', '..')
                )


@click.command()
def main():
    """Console script for filesize_from_stdin."""
    doit()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
