#!/usr/bin/python3

from eight_queens import eight_queens_dfs, eight_queens_bfs, eight_queens_sim_anneal

from eight_queens_util import gen_moves_plot

from eight_queens_min_confl import (minimum_conflicts, rand_positions, is_solution,
                                    randomly_select_conflicting_queen, move_queen_to_min_confl_pos,
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
    for i in range(10):
        soln = eight_queens_sim_anneal()
        _test_solution(soln)


def test_is_solution():
    known_good_solutions = [[0, 4, 7, 5, 2, 6, 1, 3], [0, 5, 7, 2, 6, 3, 1, 4], [0, 6, 3, 5, 7, 1, 4, 2],
                            [0, 6, 4, 7, 1, 3, 5, 2], [1, 3, 5, 7, 2, 0, 6, 4], [1, 4, 6, 0, 2, 7, 5, 3],
                            [1, 4, 6, 3, 0, 7, 5, 2], [1, 5, 0, 6, 3, 7, 2, 4], [1, 5, 7, 2, 0, 3, 6, 4],
                            [1, 6, 2, 5, 7, 4, 0, 3], [1, 6, 4, 7, 0, 3, 5, 2], [1, 7, 5, 0, 2, 4, 6, 3],
                            [2, 0, 6, 4, 7, 1, 3, 5], [2, 4, 1, 7, 0, 6, 3, 5], [2, 4, 1, 7, 5, 3, 6, 0],
                            [2, 4, 6, 0, 3, 1, 7, 5], [2, 4, 7, 3, 0, 6, 1, 5], [2, 5, 1, 4, 7, 0, 6, 3],
                            [2, 5, 1, 6, 0, 3, 7, 4], [2, 5, 1, 6, 4, 0, 7, 3], [2, 5, 3, 0, 7, 4, 6, 1],
                            [2, 5, 3, 1, 7, 4, 6, 0], [2, 5, 7, 0, 3, 6, 4, 1], [2, 5, 7, 0, 4, 6, 1, 3],
                            [2, 5, 7, 1, 3, 0, 6, 4], [2, 6, 1, 7, 4, 0, 3, 5], [2, 6, 1, 7, 5, 3, 0, 4],
                            [2, 7, 3, 6, 0, 5, 1, 4], [3, 0, 4, 7, 1, 6, 2, 5], [3, 0, 4, 7, 5, 2, 6, 1],
                            [3, 1, 4, 7, 5, 0, 2, 6], [3, 1, 6, 2, 5, 7, 0, 4], [3, 1, 6, 2, 5, 7, 4, 0],
                            [3, 1, 6, 4, 0, 7, 5, 2], [3, 1, 7, 4, 6, 0, 2, 5], [3, 1, 7, 5, 0, 2, 4, 6],
                            [3, 5, 0, 4, 1, 7, 2, 6], [3, 5, 7, 1, 6, 0, 2, 4], [3, 5, 7, 2, 0, 6, 4, 1],
                            [3, 6, 0, 7, 4, 1, 5, 2], [3, 6, 2, 7, 1, 4, 0, 5], [3, 6, 4, 1, 5, 0, 2, 7],
                            [3, 6, 4, 2, 0, 5, 7, 1], [3, 7, 0, 2, 5, 1, 6, 4], [3, 7, 0, 4, 6, 1, 5, 2],
                            [3, 7, 4, 2, 0, 6, 1, 5], [4, 0, 3, 5, 7, 1, 6, 2], [4, 0, 7, 3, 1, 6, 2, 5],
                            [4, 0, 7, 5, 2, 6, 1, 3], [4, 1, 3, 5, 7, 2, 0, 6], [4, 1, 3, 6, 2, 7, 5, 0],
                            [4, 1, 5, 0, 6, 3, 7, 2], [4, 1, 7, 0, 3, 6, 2, 5], [4, 2, 0, 5, 7, 1, 3, 6],
                            [4, 2, 0, 6, 1, 7, 5, 3], [4, 2, 7, 3, 6, 0, 5, 1], [4, 6, 0, 2, 7, 5, 3, 1],
                            [4, 6, 0, 3, 1, 7, 5, 2], [4, 6, 1, 3, 7, 0, 2, 5], [4, 6, 1, 5, 2, 0, 3, 7],
                            [4, 6, 1, 5, 2, 0, 7, 3], [4, 6, 3, 0, 2, 7, 5, 1], [4, 7, 3, 0, 2, 5, 1, 6],
                            [4, 7, 3, 0, 6, 1, 5, 2], [5, 0, 4, 1, 7, 2, 6, 3], [5, 1, 6, 0, 2, 4, 7, 3],
                            [5, 1, 6, 0, 3, 7, 4, 2], [5, 2, 0, 6, 4, 7, 1, 3], [5, 2, 0, 7, 3, 1, 6, 4],
                            [5, 2, 0, 7, 4, 1, 3, 6], [5, 2, 4, 6, 0, 3, 1, 7], [5, 2, 4, 7, 0, 3, 1, 6],
                            [5, 2, 6, 1, 3, 7, 0, 4], [5, 2, 6, 1, 7, 4, 0, 3], [5, 2, 6, 3, 0, 7, 1, 4],
                            [5, 3, 0, 4, 7, 1, 6, 2], [5, 3, 1, 7, 4, 6, 0, 2], [5, 3, 6, 0, 2, 4, 1, 7],
                            [5, 3, 6, 0, 7, 1, 4, 2], [5, 7, 1, 3, 0, 6, 4, 2], [6, 0, 2, 7, 5, 3, 1, 4],
                            [6, 1, 3, 0, 7, 4, 2, 5], [6, 1, 5, 2, 0, 3, 7, 4], [6, 2, 0, 5, 7, 4, 1, 3],
                            [6, 2, 7, 1, 4, 0, 5, 3], [6, 3, 1, 4, 7, 0, 2, 5], [6, 3, 1, 7, 5, 0, 2, 4],
                            [6, 4, 2, 0, 5, 7, 1, 3], [7, 1, 3, 0, 6, 4, 2, 5], [7, 1, 4, 2, 0, 6, 3, 5],
                            [7, 2, 0, 5, 1, 4, 6, 3], [7, 3, 0, 2, 5, 1, 6, 4]]
    for i in range(1000):
        positions = rand_positions()
        assert (positions in known_good_solutions and is_solution(positions)) \
                or (positions not in known_good_solutions and not is_solution(positions))


def test_count_conflicts():
    assert count_conflicts([6, 4, 2, 0, 5, 7, 1, 3], 7) == 0
    assert count_conflicts([4, 5, 6, 7, 0, 2, 3, 1], 5) == 1
    assert count_conflicts([0, 6, 5, 1, 3, 2, 7, 4], 2) == 3
    assert count_conflicts([4, 1, 7, 6, 5, 2, 3, 0], 3) == 3
    assert count_conflicts([0, 4, 3, 2, 5, 1, 7, 6], 2) == 4


def test_move_queen():
    positions_1 =       [6, 4, 2, 0, 5, 7, 1, 3]
    moved_positions_1 = [6, 4, 7, 0, 5, 2, 1, 3]
    assert move_queen(positions_1, 2, 5) == moved_positions_1

    positions_2 = [4, 5, 6, 7, 0, 2, 3, 1]
    moved_positions_2 = [1, 5, 6, 7, 0, 2, 3, 4]
    assert move_queen(positions_2, 0, 7) == moved_positions_2

    positions_3 = [0, 6, 5, 1, 3, 2, 7, 4]
    moved_positions_3 = [0, 6, 5, 3, 1, 2, 7, 4]
    assert move_queen(positions_3, 3, 4) == moved_positions_3

    positions_4 = [4, 1, 7, 6, 5, 3, 2, 0]
    moved_positions_4 = [4, 1, 7, 6, 5, 2, 3, 0]
    assert move_queen(positions_4, 5, 6) == moved_positions_4

    positions_5 = [6, 4, 3, 2, 5, 1, 7, 0]
    moved_positions_5 = [0, 4, 3, 2, 5, 1, 7, 6]
    assert move_queen(positions_5, 0, 7) == moved_positions_5

