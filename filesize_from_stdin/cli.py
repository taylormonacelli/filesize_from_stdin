# -*- coding: utf-8 -*-

"""Console script for filesize_from_stdin."""
import sys
import click
from .filesize_from_stdin import display_friendly, get_file_size_from_string


@click.command()
def main(args=None):
    """Console script for filesize_from_stdin."""
    display_friendly(get_file_size_from_string())


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
