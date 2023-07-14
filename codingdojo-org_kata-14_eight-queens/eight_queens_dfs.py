#!/usr/bin/python3

import random


from eight_queens_util import is_threatened


__all__ = "eight_queens_dfs",

nums_1_thru_8 = list(range(8))


def eight_queens_dfs():
    # A 1-dimensional representation of the chessboard. An index is the number
    # of the queen (and the row she's in) and a value is the column of the
    # chessboard the queen is placed in.
    positions = []

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
            if is_threatened(positions, new_queen_pos):
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

