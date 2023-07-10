#!/usr/bin/python3

import itertools


alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

goal_letter_spacing_width = dict(zip(alphabet, range(26)))


__all__ = "print_diamond",


def print_diamond(target_letter):
    if target_letter.islower():
        target_letter = target_letter.upper()

    target_letter_index = alphabet.index(target_letter)
    max_margin_cols = goal_letter_spacing_width[target_letter]

    for i in itertools.chain(range(target_letter_index + 1),
                             range(target_letter_index - 1, -1, -1)):
        margin_cols = max_margin_cols - i
        letter = alphabet[i]
        if i == 0 or i == target_letter_index * 2:
            print(" " * margin_cols, letter, sep="")
        else:
            center_cols = 2 * i - 1
            print(" " * margin_cols, letter, " " * center_cols, letter, sep="")
