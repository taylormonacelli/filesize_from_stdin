# -*- coding: utf-8 -*-

"""Console script for filesize_from_stdin."""
import sys
import click
from .filesize_from_stdin import doit


@click.command()
def main(args=None):
    """Console script for filesize_from_stdin."""
    doit()


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
