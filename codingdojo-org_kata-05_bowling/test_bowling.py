#!/usr/bin/python3

from bowling import total_scores


def test_all_strikes():
    scorings = (("X",), ("X",), ("X",), ("X",), ("X",), ("X",), ("X",), ("X",), ("X",), ("X", "X", "X"))
    score = total_scores(*scorings)
    assert score == 300

def test_all_nines():
    scorings = (("9", "-"), ("9", "-"), ("9", "-"), ("9", "-"), ("9", "-"),
                ("9", "-"), ("9", "-"), ("9", "-"), ("9", "-"), ("9", "-"))
    score = total_scores(*scorings)
    assert score == 90

def test_all_splits():
    scorings = (("5", "/"), ("5", "/"), ("5", "/"), ("5", "/"), ("5", "/"),
                ("5", "/"), ("5", "/"), ("5", "/"), ("5", "/"), ("5", "/", "5"))
    score = total_scores(*scorings)
    assert score == 150
