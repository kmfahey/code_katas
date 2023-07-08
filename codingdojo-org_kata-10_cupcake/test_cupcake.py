#!/usr/bin/python3

from cupcake import *


def test_decoration():
    foodstuff = Chocolate(Crumbled_Cookies(Crushed_Candy(Honey(Whipped_Custard(Cupcake())))))
    assert repr(foodstuff) == "Chocolate(Crumbled_Cookies(Crushed_Candy(Honey(Whipped_Custard(Cupcake())))))"
    assert foodstuff.name == "🧁 with 🍫, 🍪, 🍬, 🍯, and 🍮"

def test_name_price_1():
    foodstuff = Cupcake()
    assert foodstuff.name == "🧁"
    assert foodstuff.price == 1.00

def test_name_price_2():
    foodstuff = Cookie()
    assert foodstuff.name == "🍪"
    assert foodstuff.price == 2.00

def test_name_price_3():
    foodstuff = Chocolate(Cupcake())
    assert foodstuff.name == "🧁 with 🍫"
    assert foodstuff.price == 1.10

def test_name_price_4():
    foodstuff = Chocolate(Cookie())
    assert foodstuff.price == 2.1
    assert foodstuff.name == "🍪 with 🍫"

def test_name_price_5():
    foodstuff = Nuts(Cookie())
    assert foodstuff.price == 2.20
    assert foodstuff.name == "🍪 with 🥜"

def test_name_price_6():
    foodstuff = Nuts(Chocolate(Cookie()))
    assert foodstuff.price == 2.30
    assert foodstuff.name == "🍪 with 🥜 and 🍫"

def test_name_price_7():
    foodstuff = Chocolate(Nuts(Cookie()))
    assert foodstuff.price == 2.30
    assert foodstuff.name == "🍪 with 🍫 and 🥜"

