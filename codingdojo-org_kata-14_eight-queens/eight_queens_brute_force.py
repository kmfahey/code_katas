#!/usr/bin/python3

import random

from eight_queens_util import free_queens_kmf as free_queens


__all__ = "eight_queens_brute_force",


def shuffled(sequence):
    if isinstance(sequence, list):
        listval = sequence.copy()
    else:
        listval = list(sequence)
    random.shuffle(listval)
    return listval


def eight_queens_brute_force():
    for first in shuffled(range(8)):
        for second in shuffled(range(8)):
            for third in shuffled(range(8)):
                for fourth in shuffled(range(8)):
                    for fifth in shuffled(range(8)):
                        for sixth in shuffled(range(8)):
                            for seventh in shuffled(range(8)):
                                for eighth in shuffled(range(8)):
                                    positions = [first, second, third, fourth, fifth, sixth, seventh, eighth]
                                    if free_queens(positions) == 8:
                                        return positions
