#!/usr/bin/python3

import random
import pprint

from eight_queens_util import is_threatened


__all__ = "eight_queens_bfs",


# Recursively identifies all solutions to the eight queens problem using a
# breadth-first search.
def eight_queens_bfs():

    # Private function to do the recursion, used so it can be called with the
    # correct priming argument.
    def _8q_bfs(positions):

        # If this position list is 8 long, it comprises a valid solution and is
        # returned.
        if len(positions) == 8:
            return [positions]

        retvals = []

        # Generates the possible new queen positions using is_threatened() to
        # rule out new queen placement that would be threatened by existing
        # queens in the positions list.
        for new_queen_pos in range(8):
            if is_threatened(positions, new_queen_pos):
                continue

            # Generates a permutation with the new queen position.
            next_lvl_positions = positions + [new_queen_pos]

            # Recurses to try further queen placements. The recursive function
            # returns a list of all valid position lists generable from its
            # argument. So as the recursion completes an accumulated list of all
            # valid positions is returned.
            retvals += _8q_bfs(next_lvl_positions)

        return retvals

    return _8q_bfs([])
