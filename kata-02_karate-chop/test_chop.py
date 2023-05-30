#!/usr/bin/python3

from binary_chop_funcs import iterative_binary_chop, recursive_binary_chop, segmenting_binary_chop, indexlist_binary_chop


def test_iterative_chop():
    _test_chop(iterative_binary_chop)

def test_recursive_chop():
    _test_chop(recursive_binary_chop)

def test_segmenting_chop():
    _test_chop(segmenting_binary_chop)

def test_indexlist_chop():
    _test_chop(indexlist_binary_chop)

def _test_chop(binary_chop_func):
    assert binary_chop_func(3, []) == -1
    assert binary_chop_func(3, [1]) == -1
    assert binary_chop_func(1, [1]) == 0

    assert binary_chop_func(1, [1, 3, 5]) == 0
    assert binary_chop_func(3, [1, 3, 5]) == 1
    assert binary_chop_func(5, [1, 3, 5]) == 2
    assert binary_chop_func(0, [1, 3, 5]) == -1
    assert binary_chop_func(2, [1, 3, 5]) == -1
    assert binary_chop_func(4, [1, 3, 5]) == -1
    assert binary_chop_func(6, [1, 3, 5]) == -1

    assert binary_chop_func(1, [1, 3, 5, 7]) == 0
    assert binary_chop_func(3, [1, 3, 5, 7]) == 1
    assert binary_chop_func(5, [1, 3, 5, 7]) == 2
    assert binary_chop_func(7, [1, 3, 5, 7]) == 3
    assert binary_chop_func(0, [1, 3, 5, 7]) == -1
    assert binary_chop_func(2, [1, 3, 5, 7]) == -1
    assert binary_chop_func(4, [1, 3, 5, 7]) == -1
    assert binary_chop_func(6, [1, 3, 5, 7]) == -1
    assert binary_chop_func(8, [1, 3, 5, 7]) == -1

