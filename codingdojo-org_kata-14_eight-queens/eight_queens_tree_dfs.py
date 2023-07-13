#!/usr/bin/python3

import random


__all__ = "eight_queens_dfs",

nums_1_thru_8 = list(range(8))


def eight_queens_dfs():
    # A 1-dimensional representation of the chessboard. An index is the number
    # of the queen (and the row she's in) and a value is the column of the
    # chessboard the queen is placed in.
    positions = []

    # Given a new position for the latest queen to be placed at, returns True if
    # the new queen would be threatened there, False if she would not be.
    def _is_threatened(new_queen_pos):

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

    # Recursively with backtracking populates the positions array with queen
    # positions until it reaches len 8.
    def _eight_queens():
        # Length 8 reached, a valid solution has been found.
        if len(positions) == 8:
            return True

        # Pick new queen positions in random order, such that the algorithm can
        # return a different solution each time it's run.
        random.shuffle(nums_1_thru_8)

        for new_queen_pos in nums_1_thru_8:

            # If this position is threatened, skip it.
            if _is_threatened(new_queen_pos):
                continue

            # Otherwise try it prospectively, and see if the next position can
            # be filled.
            positions.append(new_queen_pos)

            if _eight_queens():
                # This leg of the DFS found a solution, return True all the way
                # back up the callstack.
                return True

            # This move doesn't lead to a solution, backtrack.
            positions.pop()

        # All 8 positions don't work.
        return False

    # Populates the positions array as a side effect. The recursive function is
    # a closure so no need to pass the positions var in.
    _eight_queens()

    return positions

