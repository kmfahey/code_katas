#!/usr/bin/python3

import random

from math import inf as infinity

from eight_queens_util import free_queens_kmf as free_queens, is_threatened_by_index, gen_moves_plot


__all__ = ("minimum_conflicts", "initialize_positions", "is_solution", "randomly_select_conflicting_queen",
           "move_queen_to_minimum_conflict_position", "count_conflicts", "move_queen")


# Pseudocode for minimum conflicts random walk algorithm to solve eight queens
# problem.

def minimum_conflicts(n, max_steps):
    pass

# function minimum_conflicts(n, max_steps):
#     board = initialize_positions(n)
#     for i in range(max_steps):
#         if is_solution(board):
#             return board
#         queen = randomly_select_conflicting_queen(board)
#         move_queen_to_minimum_conflict_position(queen, board)
#     return None  # No solution found within max_steps

def initialize_positions():
    positions = list(range(8))
    random.shuffle(positions)
    return positions

def is_solution(positions):
    return free_queens(positions) == 8

def randomly_select_conflicting_queen(positions):
    return random.choice(list(filter(lambda queen_index: is_threatened_by_index(positions, queen_index), range(8))))

def move_queen_to_minimum_conflict_position(queen, board):
    pass

# function move_queen_to_minimum_conflict_position(queen, board):
#     min_conflicts = infinity
#     min_conflict_positions = empty list
#     for each position in queen's column:
#         conflicts = count_conflicts(queen, position, board)
#         if conflicts < min_conflicts:
#             min_conflicts = conflicts
#             min_conflict_positions = [position]
#         else if conflicts == min_conflicts:
#             min_conflict_positions.append(position)
#     new_position = randomly_select_position_from(min_conflict_positions)
#     move_queen(queen, new_position, board)

def count_conflicts(positions, queen_index):
    conflicts = 0
    moves_plot = gen_moves_plot(queen_index, positions[queen_index])
    for row in range(8):
        col = positions[row]
        conflicts += moves_plot[row][col]
    return conflicts

def move_queen(queen, position, board):
    pass

# function move_queen(queen, position, board):
#     remove queen from its current position on the board
#     place queen at the new position on the board


