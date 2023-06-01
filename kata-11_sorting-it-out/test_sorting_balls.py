#!/usr/bin/python3


from sorting_balls import *


def test_sorting_balls():
    rack = Rack()
    assert rack.balls == []
    rack.add(20)
    assert rack.balls == [20]
    rack.add(10)
    assert rack.balls == [10, 20]
    rack.add(30)
    assert rack.balls == [10, 20, 30]

