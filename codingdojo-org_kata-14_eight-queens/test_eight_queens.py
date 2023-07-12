#!/usr/bin/python3


from eight_queens import eight_queens_dfs


# Explicit all-legal-moves generation code for a queen given initial
# coordinates. Utility function for use in testing functions to validate
# that no queen can capture any other, using very deliberate and
# explicit code that doesn't pull any tricks. (Contrast with how
# eight_queens_tree_dfs.eight_queens_dfs()'s inner function _is_threatened()
# tests for this.)
def _gen_queen_moves_coords(x_index, y_index):
    coords = list()
    if x_index < 7:
        coords.extend((modded_x_index, y_index) for modded_x_index in range(x_index + 1, 8))
        if y_index < 7:
            coords.extend((modded_x_index, modded_y_index)
                          for modded_x_index, modded_y_index
                          in zip(range(x_index + 1, 8), range(y_index + 1, 8)))
        if y_index > 0:
            coords.extend((modded_x_index, modded_y_index)
                          for modded_x_index, modded_y_index
                          in zip(range(x_index + 1, 8), range(y_index - 1, -1, -1)))
    if y_index < 7:
        coords.extend((x_index, modded_y_index) for modded_y_index in range(y_index + 1, 8))
    if y_index > 0:
        coords.extend((x_index, modded_y_index) for modded_y_index in range(y_index - 1, -1, -1))
    if x_index > 0:
        coords.extend((modded_x_index, y_index) for modded_x_index in range(x_index - 1, -1, -1))
        if y_index < 7:
            coords.extend((modded_x_index, modded_y_index)
                          for modded_x_index, modded_y_index
                          in zip(range(x_index - 1, -1, -1), range(y_index + 1, 8)))
        if y_index > 0:
            coords.extend((modded_x_index, modded_y_index)
                          for modded_x_index, modded_y_index
                          in zip(range(x_index - 1, -1, -1), range(y_index - 1, -1, -1)))
    return coords


# A utility function used to translate the output of _gen_queen_moves_coords()
# to a 2D list representing a chessboard, for visual verification of the
# validity of the output during testing of the tests.
def _gen_queen_moves_board(coords):
    board = [[0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0]]
    for coord_pair in coords:
        x_index, y_index = coord_pair
        board[x_index][y_index] = 1
    return board


# def test_eight_queens_dfs():
#     solution = eight_queens_dfs()
# 
#     chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0],
#                   [0, 0, 0, 0, 0, 0, 0, 0]]
# 
#     queen_pos = []
# 
#     for row in range(8):
#         col = solution[row]
#         chessboard[row][col] = 1
#         queens.append([row, col])
# 
#     for row, col in queen_pos:
