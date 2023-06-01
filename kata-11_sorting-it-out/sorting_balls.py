#!/usr/bin/python3


__all__ = ["Rack"]


# A rack that keeps the balls in its cache in order. Uses insertion sort to
# maintain that invariant.
class Rack:
    __slots__ = "balls",

    def __init__(self):
        self.balls = []

    def add(self, ball_number):
        if not len(self.balls):
            self.balls.append(ball_number)
        else:
            for i in range(len(self.balls)):
                if ball_number <= self.balls[i]:
                    self.balls.insert(i, ball_number)
                    return
            self.balls.append(ball_number)
