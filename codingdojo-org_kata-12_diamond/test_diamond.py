#!/usr/bin/python3

from diamond import print_diamond


def test_diamond_base_case(mocker):
    printed_lines = list()
    def record_printed_line(*line_compnts, sep=""):
        printed_lines.append(sep.join(line_compnts))
    mocker.patch("builtins.print", record_printed_line)

    print_diamond("A")

    assert printed_lines == ["A"]


def test_diamond_genl_case(mocker):
    printed_lines = list()
    def record_printed_line(*line_compnts, sep=""):
        printed_lines.append(sep.join(line_compnts))
    mocker.patch("builtins.print", record_printed_line)

    print_diamond("E")

    assert printed_lines == ["    A",
                             "   B B",
                             "  C   C",
                             " D     D",
                             "E       E",
                             " D     D",
                             "  C   C",
                             "   B B",
                             "    A"]
