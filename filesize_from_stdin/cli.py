# -*- coding: utf-8 -*-

"""Console script for filesize_from_stdin."""
import sys
import click
from .filesize_from_stdin import display_friendly, get_file_list


@click.command()
@click.argument('filename')
def main(filename):
    """Console script for filesize_from_stdin."""
    display_friendly(get_file_list(source=filename))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
