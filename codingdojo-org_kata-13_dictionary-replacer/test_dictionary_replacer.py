#!/usr/bin/python3

from pytest import raises

from dictionary_replacer import dict_replace


def test_dict_replace_1():
    string = "$foo$, $bar$, $baz$, $qux$, $quux$, $quuux$"
    dictionary = {"foo":"FOO", "bar":"BAR", "baz":"BAZ", "qux":"QUX", "quux":"QUUX", "quuux":"QUUUX"}
    rplcd_string = dict_replace(string, dictionary)
    assert rplcd_string == "FOO, BAR, BAZ, QUX, QUUX, QUUUX"


def test_dict_replace_2():
    string = ""
    dictionary = {}
    rplcd_string = dict_replace(string, dictionary)
    assert rplcd_string == ""


def test_dict_replace_3():
    string = "$temp$"
    dictionary = {"temp": "temporary"}
    rplcd_string = dict_replace(string, dictionary)
    assert rplcd_string == "temporary"


def test_dict_replace_4():
    string = "$temp$ here comes the name $name$"
    dictionary = {"temp": "temporary", "name": "John Doe"}
    rplcd_string = dict_replace(string, dictionary)
    assert rplcd_string == "temporary here comes the name John Doe"


def test_irregular_use_of_dollar_sign():
    with raises(ValueError):
        string = "   $foo$   $bar"
        dictionary = {"foo": "FOO", "bar": "BAR"}
        rplcd_string = dict_replace(string, dictionary)


def test_nonalphanumeric_tokens():
    with raises(ValueError):
        string = "   $foo$   $bar$   $rowr, bazzle$   "
        dictionary = {"foo": "FOO", "bar": "BAR"}
        rplcd_string = dict_replace(string, dictionary)
    with raises(ValueError):
        string = "   $foo$   $bar$   "
        dictionary = {"foo": "FOO", "bar": "BAR", "rowr, bazzle": "rowrbazzle"}
        rplcd_string = dict_replace(string, dictionary)


def test_irreplaceable_token():
    with raises(RuntimeError):
        string = "$foo$"
        dictionary = {}
        rplcd_string = dict_replace(string, dictionary)
