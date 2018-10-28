#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `filesize_from_stdin` package."""

import pytest

from click.testing import CliRunner

from filesize_from_stdin import filesize_from_stdin
from filesize_from_stdin import cli


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_non_empty_file(tmpdir):
    """Test file with single word in it."""
    runner = CliRunner()
    path = tmpdir.join("hello.txt")
    path.write("content")
    assert path.read() == "content"
    result = runner.invoke(cli.main, input='{}\n'.format(path))
    assert result.exit_code == 0
    assert '7B {}\n'.format(path) in result.output


def test_file_with_space(tmpdir):
    """Test file name with spaces in it."""
    runner = CliRunner()
    path = tmpdir.join("hel lo.txt")
    path.write("content")
    assert path.read() == "content"
    result = runner.invoke(cli.main, input='{}\n'.format(path))
    assert result.exit_code == 0
    assert '7B {}\n'.format(path) in result.output


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
    result = runner.invoke(cli.main, input=str(path) + '\n')
    assert result.exit_code == 0
    assert '7B {}\n'.format(path) in result.output


def test_empty_file(tmpdir):
    """Test file with no contents."""
    runner = CliRunner()
    path = tmpdir.join("hello1.txt")
    path.write("")
    assert path.read() == ""
    result = runner.invoke(cli.main, input=str(path) + '\n')
    assert result.exit_code == 0
    assert '0B {}\n'.format(path) in result.output


def test_file_does_not_exist(tmpdir):
    """Test non existant files."""
    runner = CliRunner()
    my_dir = tmpdir.mkdir("sub")
    path = os.path.join(str(my_dir), "non_existant_file.txt")
    assert not my_dir.listdir()
    result = runner.invoke(cli.main, input=str(path) + '\n')
    assert result.exit_code == 0
    assert result.output == ''


def test_no_stdin_given():
    """Here's what happens if you don't pass input."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert result.output == ''
