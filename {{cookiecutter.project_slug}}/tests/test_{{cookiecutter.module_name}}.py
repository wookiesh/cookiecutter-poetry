#!/usr/bin/env python

"""Tests for `{{ cookiecutter.module_name }}` package."""

import pytest
{%- if cookiecutter.command_line_interface | lower == "typer" %}
from typer.testing import CliRunner
{%- endif %}
{%- if cookiecutter.provide_rest_api %}
from fastapi.testclient import TestClient
{%- endif %}

from {{ cookiecutter.module_name }} import {{ cookiecutter.module_name }}
{%- if cookiecutter.command_line_interface | lower == "typer" %}
from {{ cookiecutter.module_name }} import cli
{%- endif %}


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/johanvergeer/cookiecutter-poetry')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    # assert 'GitHub' in BeautifulSoup(response.content).title.string
{%- if cookiecutter.command_line_interface | lower == "typer" %}


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "{{ cookiecutter.module_name }}.cli.main" in result.output
    help_result = runner.invoke(cli.app, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output
{%- endif %}
