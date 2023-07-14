#!/usr/bin/python3

import random

from math import inf as infinity

from eight_queens_util import free_queens_kmf as free_queens, is_threatened_by_index, gen_moves_plot


__all__ = ("minimum_conflicts", "rand_positions", "is_solution", "randomly_select_conflicting_queen",
           "move_queen_to_min_confl_pos", "count_conflicts", "move_queen")


# Pseudocode for minimum conflicts random walk algorithm to solve eight queens
# problem.

def minimum_conflicts(n, max_steps):
    pass

# function minimum_conflicts(n, max_steps):
#     board = rand_positions(n)
#     for i in range(max_steps):
#         if is_solution(board):
#             return board
#         queen = randomly_select_conflicting_queen(board)
#         move_queen_to_min_confl_pos(queen, board)
#     return None  # No solution found within max_steps

def rand_positions():
    positions = list(range(8))
    random.shuffle(positions)
    return positions


def is_solution(positions):
    return free_queens(positions) == 8


def randomly_select_conflicting_queen(positions):
    return random.choice(list(filter(lambda queen_index: is_threatened_by_index(positions, queen_index), range(8))))


def move_queen_to_min_confl_pos(positions, queen_index):
    min_conflicts = count_conflicts(positions, queen_index)
    min_confl_pos = []
    for to_index in range(8):
        if to_index == queen_index:
            continue
        new_positions = move_queen(positions, queen_index, to_index)
        conflicts = count_conflicts(new_positions, to_index)
        if conflicts < min_conflicts:
            min_conflicts = conflicts
            min_confl_pos = [to_index]
        else:
            min_confl_pos.append(to_index)
    return move_queen(positions, queen_index, random.choice(min_confl_pos))


def count_conflicts(positions, queen_index):
    conflicts = 0
    moves_plot = gen_moves_plot(queen_index, positions[queen_index])
    for row in range(8):
        col = positions[row]
        conflicts += moves_plot[row][col]
    return conflicts


def move_queen(positions, queen_from_index, queen_to_index):
    new_positions = positions.copy()
    new_positions[queen_from_index], new_positions[queen_to_index] = \
            new_positions[queen_to_index], new_positions[queen_from_index]
    return new_positions
