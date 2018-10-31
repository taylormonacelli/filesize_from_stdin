# -*- coding: utf-8 -*-

"""Console script for filesize_from_stdin."""
import sys
import click
from .filesize_from_stdin import display_friendly, get_file_list


@click.command()
@click.argument('filenames', nargs=-1, type=click.Path())
def main(filenames):
    """Console script for filesize_from_stdin."""
    if filenames:
        source = filenames[0]
    else:
        source = sys.stdin

    display_friendly(get_file_list(source))
    return 0


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
