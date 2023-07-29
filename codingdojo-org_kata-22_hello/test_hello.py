#!/usr/bin/python3

import pytest

from hello import hello_world


def test_hello_world(mocker):
    expected_output = ["Hello, world!\n"]
    output_lines = list()
    mocker.patch("builtins.print",
                 lambda *strings, sep=" ", end="\n": output_lines.append(str.join(sep, map(str, strings)) + end))
    hello_world()
    assert output_lines == expected_output
