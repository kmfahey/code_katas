#!/usr/bin/python3


__all__ = "is_threatened",


# Given a new position for the latest queen to be placed at, returns True if
# the new queen would be threatened there, False if she would not be.
def is_threatened(positions, new_queen_pos):

    for i, queen_pos in enumerate(positions):
        # New queen is in the same column as this previously placed queen.
        if queen_pos == new_queen_pos:
            return True

        # Quoth ChatGPT-4, which wrote this function: "If the absolute
        # difference between the columns of the newly placed queen and
        # any of the previously placed queens is equal to the absolute
        # difference between their respective row positions, it means they
        # are on the same diagonal and can threaten each other."
        if abs(queen_pos - new_queen_pos) == abs(i - len(positions)):
            return True

    return False
