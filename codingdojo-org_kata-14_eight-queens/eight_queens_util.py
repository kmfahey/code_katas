#!/usr/bin/python3


__all__ = "is_threatened", "free_queens_kmf", "is_threatened_by_index", "gen_moves_plot"


def is_threatened_by_index(positions, queen_index):
    return is_threatened(positions[:queen_index], positions[queen_index], positions[queen_index+1:])


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


def gen_moves_plot(row, col):
    coords = list()

    # Explicit all-legal-moves generation code for a queen given initial
    # coordinates. Utility function for use in testing functions to validate
    # that no queen can capture any other, using very deliberate and
    # explicit code that doesn't pull any tricks. (Contrast with how
    # eight_queens_dfs.eight_queens_dfs()'s inner function _is_threatened()
    # tests for this.)

    # South
    if row < 7:
        coords.extend((incr_row, col) for incr_row in range(row + 1, 8))
        # Southeast
        if col < 7:
            coords.extend((incr_row, incr_col) for incr_row, incr_col
                          in zip(range(row + 1, 8), range(col + 1, 8)))
        # Southwest
        if col > 0:
            coords.extend((incr_row, decr_col) for incr_row, decr_col
                          in zip(range(row + 1, 8), range(col - 1, -1, -1)))
    # East
    if col < 7:
        coords.extend((row, incr_col) for incr_col in range(col + 1, 8))
    # West
    if col > 0:
        coords.extend((row, decr_col) for decr_col in range(col - 1, -1, -1))
    # North
    if row > 0:
        coords.extend((decr_row, col) for decr_row in range(row - 1, -1, -1))
        # Northeast
        if col < 7:
            coords.extend((decr_row, incr_col) for decr_row, incr_col
                          in zip(range(row - 1, -1, -1), range(col + 1, 8)))
        # Northwest
        if col > 0:
            coords.extend((decr_row, decr_col) for decr_row, decr_col
                          in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)))

    # Plots the coordinates on a list-of-lists that represents a chessboard.
    moves_plot = [list((0,)*8) for _ in range(8)]

    for (row, col) in coords:
        moves_plot[row][col] = 1

    return moves_plot


