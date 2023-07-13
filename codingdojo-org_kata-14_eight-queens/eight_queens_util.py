#!/usr/bin/python3


__all__ = "is_threatened", "free_queens_kmf"


# Given a new position for the latest queen to be placed at, returns True if
# the new queen would be threatened there, False if she would not be.
def is_threatened(left_positions, new_queen_pos, right_positions=()):

    enumerated = list(enumerate(left_positions))

    if len(right_positions):
        offset = len(left_positions) + 1
        enumerated += list(enumerate(right_positions, start=offset))

    for i, queen_pos in enumerated:
        # New queen is in the same column as this previously placed queen.
        if queen_pos == new_queen_pos:
            return True

        # Quoth ChatGPT-4, which wrote this function: "If the absolute
        # difference between the columns of the newly placed queen and
        # any of the previously placed queens is equal to the absolute
        # difference between their respective row positions, it means they
        # are on the same diagonal and can threaten each other."
        if abs(queen_pos - new_queen_pos) == abs(i - len(left_positions)):
            return True

    return False


def free_queens_kmf(positions):
    return 8 - sum(is_threatened(positions[:i], positions[i], positions[i+1:]) for i in range(8))
