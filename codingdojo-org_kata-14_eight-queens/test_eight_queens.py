#!/usr/bin/python3

from eight_queens import eight_queens_dfs, eight_queens_bfs


def gen_moves_plot(row, col):
    coords = list()

    # Explicit all-legal-moves generation code for a queen given initial
    # coordinates. Utility function for use in testing functions to validate
    # that no queen can capture any other, using very deliberate and
    # explicit code that doesn't pull any tricks. (Contrast with how
    # eight_queens_tree_dfs.eight_queens_dfs()'s inner function _is_threatened()
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


def _test_solution(soln):
    moves_plots = {(row, soln[row]): gen_moves_plot(row, soln[row]) for row in range(8)}

    assert not any(moves_plot[row][col]
                   for coord, moves_plot in moves_plots.items()
                   for row, col in moves_plots.keys()
                   if (row, col) != coord)


def test_eight_queens_dfs():
    soln = eight_queens_dfs()
    _test_solution(soln)


def test_eight_queens_bfs():
    for soln in eight_queens_bfs():
        _test_solution(soln)
