#!/usr/bin/python3


from checkout import *


PRICING_RULES = {
    "A": [Rule(1, 50), Rule(3, 130)],
    "B": [Rule(1, 30), Rule(2, 45)],
    "C": [Rule(1, 20)],
    "D": [Rule(1, 15)]
}


def price(goods):
    checkout = Checkout(PRICING_RULES)
    for good in goods:
        checkout.scan(good)
    return checkout.total()


def test_totals():
    assert price("") == 0
    assert price("A") == 50
    assert price("AB") == 80
    assert price("CDBA") == 115

    assert price("AA") == 100
    assert price("AAA") == 130
    assert price("AAAA") == 180
    assert price("AAAAA") == 230
    assert price("AAAAAA") == 260

    assert price("AAAB") == 160
    assert price("AAABB") == 175
    assert price("AAABBD") == 190
    assert price("DABABA") == 190


def test_incremental():
    checkout = Checkout(PRICING_RULES)
    assert checkout.total() == 0
    checkout.scan("A")
    assert checkout.total() == 50
    checkout.scan("B")
    assert checkout.total() == 80
    checkout.scan("A")
    assert checkout.total() == 130
    checkout.scan("A")
    assert checkout.total() == 160
    checkout.scan("B")
    assert checkout.total() == 175
