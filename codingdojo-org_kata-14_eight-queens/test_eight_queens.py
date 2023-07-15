#!/usr/bin/python3

import random

from eight_queens import eight_queens_dfs, eight_queens_bfs, eight_queens_sim_anneal, eight_queens_min_confl

from eight_queens_util import gen_moves_plot


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
    soln = eight_queens_bfs()
    _test_solution(soln)


def test_eight_queens_sim_anneal():
    for i in range(10):
        soln = eight_queens_sim_anneal()
        _test_solution(soln)


def test_eight_queens_min_confl():
    for i in range(10):
        soln = eight_queens_min_confl()
        _test_solution(soln)


if __name__ == "__main__":
    soln = eight_queens_min_confl()
    print(soln)

