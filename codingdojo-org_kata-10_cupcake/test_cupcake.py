#!/usr/bin/python3

from cupcake import *


sideline = open("sideline.txt", "w")


def test_decoration():
    foodstuff = Chocolate(Crumbled_Cookies(Crushed_Candy(Honey(Whipped_Custard(Cupcake())))))
    assert repr(foodstuff) == "Chocolate(Crumbled_Cookies(Crushed_Candy(Honey(Whipped_Custard(Cupcake())))))"
    assert foodstuff.name == "🧁 with 🍫, 🍪, 🍬, 🍯, and 🍮"

def test_decorable_name_price_1():
    foodstuff = Cupcake()
    assert foodstuff.name == "🧁"
    assert foodstuff.price == 1.00

def test_decorable_name_price_2():
    foodstuff = Cookie()
    assert foodstuff.name == "🍪"
    assert foodstuff.price == 2.00

def test_decorable_name_price_3():
    foodstuff = Chocolate(Cupcake())
    assert foodstuff.name == "🧁 with 🍫"
    assert foodstuff.price == 1.10

def test_decorable_name_price_4():
    foodstuff = Chocolate(Cookie())
    assert foodstuff.price == 2.1
    assert foodstuff.name == "🍪 with 🍫"

def test_decorable_name_price_5():
    foodstuff = Nuts(Cookie())
    assert foodstuff.price == 2.20
    assert foodstuff.name == "🍪 with 🥜"

def test_decorable_name_price_6():
    foodstuff = Nuts(Chocolate(Cookie()))
    assert foodstuff.price == 2.30
    assert foodstuff.name == "🍪 with 🥜 and 🍫"

def test_decorable_name_price_7():
    foodstuff = Chocolate(Nuts(Cookie()))
    assert foodstuff.price == 2.30
    assert foodstuff.name == "🍪 with 🍫 and 🥜"

def test_bundle_1():
    bundle = Bundle([Cupcake()])
    assert bundle.price == 0.90
    assert bundle.description == "a bundle that contains 1 🧁\n"

def test_bundle_2():
    bundle = Bundle([Cupcake(), Cookie()])
    assert bundle.price == 2.70
    assert bundle.description == \
"""a bundle that contains:
    - 1 🧁
    - 1 🍪
"""

def test_bundle_3():
    bundle = Bundle([Cupcake(), Cupcake(), Cookie()])
    assert bundle.price == 3.60
    assert bundle.description == \
"""a bundle that contains:
    - 2 🧁
    - 1 🍪
"""

def test_bundle_4():
    bundle = Bundle([Bundle([Cake(), Cake()]), Cupcake()])
    assert bundle.price == 17.10
    assert bundle.description == \
"""a bundle that contains:
    - a bundle that contains 2 🎂
    - 1 🧁
"""

def test_bundle_5():
    bundle = Bundle([Bundle([Cake(), Cake(), Cake()]),
                     Bundle([Cake(), Cake(), Cake()]),
                     Bundle([Cake(), Cake(), Cake()])])
    assert bundle.price == 72.90
    assert bundle.description == \
"""a bundle that contains:
    - a bundle that contains 3 🎂
    - a bundle that contains 3 🎂
    - a bundle that contains 3 🎂
"""
