#!/usr/bin/python3

from eight_queens import eight_queens_dfs, eight_queens_bfs, eight_queens_sim_anneal

from eight_queens_util import gen_moves_plot

from eight_queens_min_confl import (minimum_conflicts, initialize_positions, is_solution,
                                    randomly_select_conflicting_queen, move_queen_to_minimum_conflict_position,
                                    count_conflicts, move_queen)


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


def test_eight_queens_sim_anneal():
    for i in range(100):
        soln = eight_queens_sim_anneal()
        _test_solution(soln)
