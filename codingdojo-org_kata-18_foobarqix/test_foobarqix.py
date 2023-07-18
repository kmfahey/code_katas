#!/usr/bin/python3


from foobarqix import compute


def test_compute_1():
    assert compute("1") == "1"
    assert compute("2") == "2"
    assert compute("3") == "FooFoo"
    assert compute("4") == "4"
    assert compute("5") == "BarBar"
    assert compute("6") == "Foo"
    assert compute("7") == "QixQix"
    assert compute("8") == "8"
    assert compute("9") == "Foo"
    assert compute("10") == "Bar*"
    assert compute("13") == "Foo"
    assert compute("15") == "FooBarBar"
    assert compute("21") == "FooQix"
    assert compute("33") == "FooFooFoo"
    assert compute("51") == "FooBar"
    assert compute("53") == "BarFoo"


def test_compute_2():
    assert compute("101") == "1*1"
    assert compute("303") == "FooFoo*Foo"
    assert compute("105") == "FooBarQix*Bar"
    assert compute("10101") == "FooQix**"
