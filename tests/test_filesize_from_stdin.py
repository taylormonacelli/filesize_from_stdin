#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `filesize_from_stdin` package."""

import pytest

from click.testing import CliRunner
from filesize_from_stdin import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_file_list_as_argument_and_fed_through_stdin(tmpdir):
    """Test file with single word in it."""
    runner = CliRunner()

    path1 = tmpdir.join("tmpfile1.txt")
    path1.write("content")

    path2 = tmpdir.join("tmpfile2.txt")
    path2.write("hel")

    path3 = tmpdir.join("tmpfile3.txt")
    path3.write("a")

    path4 = tmpdir.join("tmpfile4.txt")
    path4.write("hello")

    result = runner.invoke(
        cli.main, [
            str(path1), str(path2)], input='{}\n{}'.format(path3, path4))

    assert result.exit_code == 0
    assert '7B {}'.format(path1) in result.output
    assert '3B {}'.format(path2) in result.output
    assert '1B {}'.format(path3) in result.output
    assert '5B {}'.format(path4) in result.output


def test_file_list_as_argument_but_doesnt_exist(tmpdir):
    """Test file with single word in it."""
    runner = CliRunner()
    # generate file path, but don't create file
    path = tmpdir.join("tmpfile1.txt")

    result = runner.invoke(cli.main, str(path))

    assert result.exit_code == 0
    assert '' == result.output


def test_file_list_as_argument(tmpdir):
    """Test file with single word in it."""
    runner = CliRunner()

    path1 = tmpdir.join("tmpfile1.txt")
    path1.write("content")

    path2 = tmpdir.join("tmpfile2.txt")
    path2.write("hel")

    result = runner.invoke(cli.main, [str(path1), str(path2)])

    assert result.exit_code == 0
    assert '7B {}'.format(path1) in result.output
    assert '3B {}'.format(path2) in result.output


def test_non_empty_file(tmpdir):
    """Test file with single word in it."""
    runner = CliRunner()
    path = tmpdir.join("hello.txt")
    path.write("content")
    assert path.read() == "content"
    result = runner.invoke(cli.main, input=str(path))
    assert result.exit_code == 0
    assert '7B {}'.format(path) in result.output


def test_file_with_space(tmpdir):
    """Test file name with spaces in it."""
    runner = CliRunner()
    path = tmpdir.join("hel lo.txt")
    path.write("content")
    assert path.read() == "content"
    result = runner.invoke(cli.main, input=str(path))
    assert result.exit_code == 0
    assert '7B {}'.format(path) in result.output


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output


def test_file_with_quote_in_name(tmpdir):
    """Test the CLI."""
    runner = CliRunner()
    path = tmpdir.join("hello'.txt")
    path.write("content")
    assert path.read() == "content"
    result = runner.invoke(cli.main, input=str(path))
    assert result.exit_code == 0
    assert '7B {}'.format(path) in result.output


def test_empty_file(tmpdir):
    """Test file with no contents."""
    runner = CliRunner()
    path = tmpdir.join("hello1.txt")
    path.write("")
    assert path.read() == ""
    result = runner.invoke(cli.main, input=str(path))
    assert result.exit_code == 0
    assert '0B {}'.format(path) in result.output


def test_file_does_not_exist(tmpdir):
    """Test non existant files."""
    runner = CliRunner()
    sub = tmpdir.mkdir("sub")
    path = sub.join("non_existant_file.txt")
    assert not sub.listdir()
    result = runner.invoke(cli.main, input=str(path))
    assert result.exit_code == 0
    assert result.output == ''


def test_no_stdin_given():
    """Here's what happens if you don't pass input."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert result.output == ''
