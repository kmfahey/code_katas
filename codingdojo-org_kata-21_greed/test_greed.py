#!/usr/bin/python3

from greed import Greed


def test_no_score():
    assert Greed().score([3, 2, 6, 2, 3, 4]) == 0


def test_single_1():
    assert Greed().score([3, 2, 4, 1, 2, 4]) == 100

def test_single_5():
    assert Greed().score([3, 2, 4, 5, 2, 4]) == 50

def test_single_1_single_5():
    assert Greed().score([6, 5, 4, 1, 3, 3]) == 100 + 50


def test_double_1s():
    assert Greed().score([2, 6, 5, 5, 4, 6]) == 100
    assert Greed().score([2, 5, 1, 1, 4, 6]) == 50 + 200


def test_triple_1s():
    assert Greed().score([1, 6, 1, 1, 3, 6]) == 1000
    assert Greed().score([1, 1, 4, 5, 1, 2]) == 1000 + 50

def test_quadruple_1s():
    assert Greed().score([6, 5, 1, 1, 1, 1]) == 50 + 1000*2
    assert Greed().score([1, 1, 6, 3, 1, 1]) == 1000*2

def test_quintuple_1s():
    assert Greed().score([6, 1, 1, 1, 1, 1]) == 1000*4

def test_sextuple_1s():
    assert Greed().score([1, 1, 1, 1, 1, 1]) == 1000*8



def test_triple_2s():
    assert Greed().score([2, 2, 5, 3, 6, 2]) == 50 + 200
    assert Greed().score([1, 5, 2, 2, 2, 6]) == 200 + 100 + 50

def test_quadruple_2s():
    assert Greed().score([6, 5, 2, 2, 2, 2]) == 50 + 200*2
    assert Greed().score([2, 2, 6, 3, 2, 2]) == 200*2

def test_quintuple_2s():
    assert Greed().score([6, 2, 2, 2, 2, 2]) == 200*4

def test_sextuple_2s():
    assert Greed().score([2, 2, 2, 2, 2, 2]) == 200*8


def test_triple_3s():
    assert Greed().score([3, 4, 3, 2, 3, 4]) == 300
    assert Greed().score([3, 1, 3, 2, 3, 2]) == 100 + 300

def test_quadruple_3s():
    assert Greed().score([6, 5, 3, 3, 3, 3]) == 50 + 300*2

def test_quintuple_3s():
    assert Greed().score([6, 3, 3, 3, 3, 3]) == 300*4

def test_sextuple_3s():
    assert Greed().score([3, 3, 3, 3, 3, 3]) == 300*8


def test_triple_4s():
    assert Greed().score([4, 4, 4, 3, 6, 1]) == 100 + 400
    assert Greed().score([4, 4, 5, 1, 4, 6]) == 50 + 100 + 400

def test_quadruple_4s():
    assert Greed().score([4, 4, 1, 3, 4, 4]) == 100 + 400*2

def test_quintuple_4s():
    assert Greed().score([4, 4, 4, 3, 4, 4]) == 400*4

def test_sextuple_4s():
    assert Greed().score([4, 4, 4, 4, 4, 4]) == 400*8


def test_triple_5s():
    assert Greed().score([5, 5, 5, 3, 6, 1]) == 100 + 500
    assert Greed().score([5, 5, 5, 2, 2, 6]) == 500

def test_quadruple_2s():
    assert Greed().score([6, 6, 5, 5, 5, 5]) == 500*2
    assert Greed().score([5, 5, 6, 3, 5, 5]) == 500*2

def test_quintuple_2s():
    assert Greed().score([6, 5, 5, 5, 5, 5]) == 500*4

def test_sextuple_2s():
    assert Greed().score([5, 5, 5, 5, 5, 5]) == 500*8



def test_triple_6s():
    assert Greed().score([2, 1, 6, 3, 6, 6]) == 100 + 600

def test_quadruple_2s():
    assert Greed().score([2, 2, 6, 6, 6, 6]) == 600*2
    assert Greed().score([6, 6, 2, 3, 6, 6]) == 600*2

def test_quintuple_2s():
    assert Greed().score([2, 6, 6, 6, 6, 6]) == 600*4

def test_sextuple_2s():
    assert Greed().score([6, 6, 6, 6, 6, 6]) == 600*8



def test_three_pairs():
    assert Greed().score([1, 5, 6, 1, 6, 5]) == 800
    assert Greed().score([2, 2, 5, 5, 6, 6]) == 800


def test_straight():
    assert Greed().score([1, 2, 3, 4, 5, 6]) == 1200
