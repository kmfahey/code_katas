#!/usr/bin/python3

from math import inf


# Using every form of graph representation except OO, so that I get experience
# writing the same graph algorithm for each one.

# ONE-NODE TRIVIAL GRAPH

# adjacency matrix
one_node_adjmx = [[inf]]

# adjacency list
one_node_adjl = [[]]

# edge list
one_node_edgl = []

# incidence matrix
one_node_incmx = [[]]

# adjacency map
one_node_adjl = [{}]


# ADJACENCY MATRIXES

# adjacency matrix
two_node_adjmx = [[inf, 1],
                  [1,   inf]]

# adjacency list
two_node_adjl = [[2],
                 [1]]

# edge list
two_node_edgl = [(1, 2)]

# incidence matrix
two_node_incmx = [[1],
                  [1]]

# adjacency map
two_node_adjl = [{2: True},
                 {1: True}]


# 2 X 2 MAZE
# 
# 1 - 2
# |
# 3 - 4

# adjacency matrix
                 # 1    2    3    4
maze_2x2_adjmx = [[inf, 1,   1,   0],   # 1
                  [1,   inf, 0,   0],   # 2
                  [1,   0,   inf, 1],   # 3
                  [0,   0,   1,   inf]] # 4

# adjacency list
maze_2x2_adjl = [[2, 3],
                 [1],
                 [1, 4],
                 [3]]

# edge list
maze_2x2_edgl = [(1, 2),
                 (1, 3),
                 (3, 4)]

# incidence matrix
# 
# 1 a 2
# b
# 3 c 4
                 # edges
                 # a  b  c
maze_2x2_incmx = [[1, 0, 0], # 1
                  [1, 1, 0], # 2
                  [0, 1, 1]] # 3

# adjacency map
maze_2x2_adjl = [{2: True, 3: True},
                 {1: True},
                 {1: True, 4: True},
                 {3: True}]


# BINARY TREE

# adjacency matrix
#                     1    2    3    4    5    6    7
binary_tree_adjmx = [[inf, 1,   1,   0,   0,   0,   0],   # 1
                     [1,   inf, 0,   1,   1,   0,   0],   # 2
                     [1,   0,   inf, 0,   0,   1,   1],   # 3
                     [0,   1,   0,   inf, 0,   0,   0],   # 4
                     [0,   1,   0,   0,   inf, 0,   0],   # 5
                     [0,   0,   1,   0,   0,   inf, 0],   # 6
                     [0,   0,   1,   0,   0,   0,   inf]] # 7

# adjacency list
binary_tree_adjl = [[2, 3],
                    [1, 4, 5],
                    [1, 6, 7],
                    [2],
                    [2],
                    [3],
                    [3]]

# edge list
binary_tree_edgl = [(1, 2),
                    (1, 3),
                    (2, 4),
                    (2, 5),
                    (3, 6),
                    (3, 7)]

# incidence matrix
#            1
#          a   b
#        2       3
#       c d     e f
#      4   5   6   7
#                     a  b  c  d  e  f
binary_tree_incmx = [[1, 1, 0, 0, 0, 0], # 1
                     [1, 0, 1, 1, 0, 0], # 2
                     [0, 1, 0, 0, 1, 1], # 3
                     [0, 0, 1, 0, 0, 0], # 4
                     [0, 0, 0, 1, 0, 0], # 5
                     [0, 0, 0, 0, 1, 0], # 6
                     [0, 0, 0, 0, 0, 1]] # 7


# adjacency map
binary_tree_adjl = [{2: True, 3: True},
                    {1: True, 4: True, 5: True},
                    {1: True, 6: True, 7: True},
                    {2: True},
                    {2: True},
                    {3: True},
                    {3: True}]


# 3 X 3 MAZE

# adjacency matrix
#                  1    2    3    4    5    6    7    8    9
maze_3x3_adjmx = [[inf, 1,   0,   0,   0,   0,   0,   0,   0],   # 1
                  [1,   inf, 1,   0,   1,   0,   0,   0,   0],   # 2
                  [0,   1,   inf, 0,   0,   0,   0,   0,   0],   # 3
                  [0,   0,   0,   inf, 0,   0,   1,   0,   0],   # 4
                  [0,   1,   0,   0,   inf, 1,   0,   1,   0],   # 5
                  [0,   0,   0,   0,   1,   inf, 0,   0,   1],   # 6
                  [0,   0,   0,   1,   0,   0,   inf, 1,   0],   # 7
                  [0,   0,   0,   0,   1,   0,   1,   inf, 1],   # 8
                  [0,   0,   0,   0,   0,   1,   0,   1,   inf]] # 9

# adjacency list
maze_3x3_adjl = [[2],
                 [1, 3, 5],
                 [2],
                 [7],
                 [2, 6, 8],
                 [5, 9],
                 [4],
                 [5, 7, 9],
                 [6, 8]]

# edge list
maze_3x3_edgl = [(1, 2),
                 (2, 3),
                 (2, 5),
                 (4, 7),
                 (5, 8),
                 (6, 9),
                 (7, 8),
                 (8, 9)]


# incidence matrix
# 
# 1 a 2 b 3
#     c    
# 4   5 d 6
# e   f   g
# 7 h 8 i 9
#                  a  b  c  d  e  f  g  h  i
maze_3x3_adjmx = [[1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
                  [1, 1, 1, 0, 0, 0, 0, 0, 0], # 2
                  [0, 1, 0, 0, 0, 0, 0, 0, 0], # 3
                  [0, 0, 0, 0, 1, 0, 0, 0, 0], # 4
                  [0, 0, 1, 1, 0, 1, 0, 0, 0], # 5
                  [0, 0, 0, 1, 0, 0, 1, 0, 0], # 6
                  [0, 0, 0, 0, 1, 0, 0, 1, 0], # 7
                  [0, 0, 0, 0, 0, 1, 0, 1, 1], # 8
                  [0, 0, 0, 0, 0, 0, 1, 0, 1]] # 9


# adjacency map
gaze_3x3_adjl = [{2: True},
                 {1: True, 3: True, 5: True},
                 {2: True},
                 {7: True},
                 {2: True, 6: True, 8: True},
                 {5: True, 9: True},
                 {4: True},
                 {5: True, 7: True, 9: True},
                 {6: True, 8: True}]
