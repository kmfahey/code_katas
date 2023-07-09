#!/usr/bin/python3

from math import inf


ONE_NODE_GRAPH = 1
TWO_NODE_GRAPH = 2
MAZE_2_X_2 = 3
BINARY_TREE = 4
MAZE_3_X_3 = 5

ADJ_MX = 6
ADJ_LIST = 7
EDGE_LIST = 8
INC_MX = 9
ADJ_MAP = 10

test_graphs = {
        ONE_NODE_GRAPH: dict.fromkeys((ADJ_MX, ADJ_LIST, EDGE_LIST, INC_MX, ADJ_MAP)),
        TWO_NODE_GRAPH: dict.fromkeys((ADJ_MX, ADJ_LIST, EDGE_LIST, INC_MX, ADJ_MAP)),
        MAZE_2_X_2: dict.fromkeys((ADJ_MX, ADJ_LIST, EDGE_LIST, INC_MX, ADJ_MAP)),
        BINARY_TREE: dict.fromkeys((ADJ_MX, ADJ_LIST, EDGE_LIST, INC_MX, ADJ_MAP)),
        MAZE_3_X_3: dict.fromkeys((ADJ_MX, ADJ_LIST, EDGE_LIST, INC_MX, ADJ_MAP)),
        }


# Using every form of graph representation except OO, so that I get experience
# writing the same graph algorithm for each one.

# ONE-NODE TRIVIAL GRAPH

# adjacency matrix
test_graphs[ONE_NODE_GRAPH][ADJ_MX] = [[inf]]

# adjacency list
test_graphs[ONE_NODE_GRAPH][ADJ_LIST] = [[]]

# edge list
test_graphs[ONE_NODE_GRAPH][EDGE_LIST] = []

# incidence matrix
test_graphs[ONE_NODE_GRAPH][INC_MX] = [[]]

# adjacency map
test_graphs[ONE_NODE_GRAPH][ADJ_MAP] = [{}]


# ADJACENCY MATRIXES

# adjacency matrix
test_graphs[TWO_NODE_GRAPH][ADJ_MX] = [[inf, 1], [1,   inf]]

# adjacency list
test_graphs[TWO_NODE_GRAPH][ADJ_LIST] = [[2], [1]]

# edge list
test_graphs[TWO_NODE_GRAPH][EDGE_LIST] = [(1, 2)]

# incidence matrix
test_graphs[TWO_NODE_GRAPH][INC_MX] = [[1], [1]]

# adjacency map
test_graphs[TWO_NODE_GRAPH][ADJ_MAP] = [{2: True}, {1: True}]


# 2 X 2 MAZE
# 
# 1 - 2
# |
# 3 - 4

# adjacency matrix
                 # 1    2    3    4
test_graphs[MAZE_2_X_2][ADJ_MX] = [[inf, 1,   1,   0],   # 1
                                   [1,   inf, 0,   0],   # 2
                                   [1,   0,   inf, 1],   # 3
                                   [0,   0,   1,   inf]] # 4

# adjacency list
test_graphs[MAZE_2_X_2][ADJ_LIST] = [[2, 3], [1], [1, 4], [3]]

# edge list
test_graphs[MAZE_2_X_2][EDGE_LIST] = [(1, 2), (1, 3), (3, 4)]

# incidence matrix
# 
# 1 a 2
# b
# 3 c 4
                 # edges
                 # a  b  c
test_graphs[MAZE_2_X_2][INC_MX] = [[1, 0, 0], # 1
                                   [1, 1, 0], # 2
                                   [0, 1, 1]] # 3

# adjacency map
test_graphs[MAZE_2_X_2][ADJ_MAP] = [{2: True, 3: True}, {1: True}, {1: True, 4: True}, {3: True}]


# BINARY TREE

# adjacency matrix
#                     1    2    3    4    5    6    7
test_graphs[BINARY_TREE][ADJ_MX] = [[inf, 1,   1,   0,   0,   0,   0],   # 1
                                    [1,   inf, 0,   1,   1,   0,   0],   # 2
                                    [1,   0,   inf, 0,   0,   1,   1],   # 3
                                    [0,   1,   0,   inf, 0,   0,   0],   # 4
                                    [0,   1,   0,   0,   inf, 0,   0],   # 5
                                    [0,   0,   1,   0,   0,   inf, 0],   # 6
                                    [0,   0,   1,   0,   0,   0,   inf]] # 7

# adjacency list
test_graphs[BINARY_TREE][ADJ_LIST] = [[2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3], [3]]

# edge list
test_graphs[BINARY_TREE][EDGE_LIST] = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7)]

# incidence matrix
#            1
#          a   b
#        2       3
#       c d     e f
#      4   5   6   7
#                     a  b  c  d  e  f
test_graphs[BINARY_TREE][INC_MX] = [[1, 1, 0, 0, 0, 0], # 1
                                    [1, 0, 1, 1, 0, 0], # 2
                                    [0, 1, 0, 0, 1, 1], # 3
                                    [0, 0, 1, 0, 0, 0], # 4
                                    [0, 0, 0, 1, 0, 0], # 5
                                    [0, 0, 0, 0, 1, 0], # 6
                                    [0, 0, 0, 0, 0, 1]] # 7


# adjacency map
test_graphs[BINARY_TREE][ADJ_MAP] = [{2: True, 3: True}, {1: True, 4: True, 5: True}, {1: True, 6: True, 7: True},
                                     {2: True}, {2: True}, {3: True}, {3: True}]


# 3 X 3 MAZE

# adjacency matrix
#                  1    2    3    4    5    6    7    8    9
test_graphs[MAZE_3_X_3][ADJ_MX] = [[inf, 1,   0,   0,   0,   0,   0,   0,   0],   # 1
                                   [1,   inf, 1,   0,   1,   0,   0,   0,   0],   # 2
                                   [0,   1,   inf, 0,   0,   0,   0,   0,   0],   # 3
                                   [0,   0,   0,   inf, 0,   0,   1,   0,   0],   # 4
                                   [0,   1,   0,   0,   inf, 1,   0,   1,   0],   # 5
                                   [0,   0,   0,   0,   1,   inf, 0,   0,   1],   # 6
                                   [0,   0,   0,   1,   0,   0,   inf, 1,   0],   # 7
                                   [0,   0,   0,   0,   1,   0,   1,   inf, 1],   # 8
                                   [0,   0,   0,   0,   0,   1,   0,   1,   inf]] # 9

# adjacency list
test_graphs[MAZE_3_X_3][ADJ_LIST] = [[2], [1, 3, 5], [2], [7], [2, 6, 8], [5, 9], [4], [5, 7, 9], [6, 8]]

# edge list
test_graphs[MAZE_3_X_3][EDGE_LIST] = [(1, 2), (2, 3), (2, 5), (4, 7), (5, 8), (6, 9), (7, 8), (8, 9)]


# incidence matrix
# 
# 1 a 2 b 3
#     c    
# 4   5 d 6
# e   f   g
# 7 h 8 i 9
#                  a  b  c  d  e  f  g  h  i
test_graphs[MAZE_3_X_3][ADJ_MX] = [[1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
                                   [1, 1, 1, 0, 0, 0, 0, 0, 0], # 2
                                   [0, 1, 0, 0, 0, 0, 0, 0, 0], # 3
                                   [0, 0, 0, 0, 1, 0, 0, 0, 0], # 4
                                   [0, 0, 1, 1, 0, 1, 0, 0, 0], # 5
                                   [0, 0, 0, 1, 0, 0, 1, 0, 0], # 6
                                   [0, 0, 0, 0, 1, 0, 0, 1, 0], # 7
                                   [0, 0, 0, 0, 0, 1, 0, 1, 1], # 8
                                   [0, 0, 0, 0, 0, 0, 1, 0, 1]] # 9


# adjacency map
test_graphs[MAZE_3_X_3][ADJ_MAP] = [{2: True}, {1: True, 3: True, 5: True}, {2: True}, {7: True},
                                    {2: True, 6: True, 8: True}, {5: True, 9: True}, {4: True},
                                    {5: True, 7: True, 9: True}, {6: True, 8: True}]
