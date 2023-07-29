#!/usr/bin/python3

import attr


__all__ = "Greed",


@attr.s
class Greed:
    def _validate_total_score(self, attribute, value):
        if value < 0:
            raise ValueError("value for score must not be less than 0")

    total_score = attr.ib(type=int, default=0, validator=attr.validators.and_(attr.validators.instance_of(int),
                                                                              _validate_total_score))

    def score(self, dice):
        if len(dice) > 6:
            raise ValueError("sequence value for dice must not be longer than 6 elements")
        elif not all(isinstance(elem, int) for elem in dice):
            raise ValueError("all elements of dice must be integers")

        dice = sorted(dice.copy())
        if dice == [1, 2, 3, 4, 5, 6]:
            self.total_score += 1200
            return 1200
        elif triples := (dice[0] == dice[1] and
                         dice[1] != dice[2] and
                         dice[2] == dice[3] and
                         dice[3] != dice[4] and
                         dice[4] == dice[5]):
            running_score = 800
        else:
            running_score = 0

        match dice.count(1):
            case 1:
                running_score += 100
            case 2 if not triples:
                running_score += 200
            case 3 | 4 | 5 | 6 as count:
                running_score += 1000 * int(2**(count - 3))
        if (count := dice.count(2)) >= 3:
            running_score += 200 * int(2**(count - 3))
        if (count := dice.count(3)) >= 3:
            running_score += 300 * int(2**(count - 3))
        if (count := dice.count(4)) >= 3:
            running_score += 400 * int(2**(count - 3))
        match dice.count(5):
            case 1:
                running_score += 50
            case 2 if not triples:
                running_score += 50*2
            case 3 | 4 | 5 | 6 as count:
                running_score += 500 * int(2**(count - 3))
        if (count := dice.count(6)) >= 3:
            running_score += 600 * int(2**(count - 3))

        self.total_score += running_score
        return running_score
