#!/usr/bin/python3

from math import inf

from depth_first_search import *


# The *_adj_nodes() functions return the adjacent nodes in numeric order.
# Because iter_dfs() pushes the nodes onto the stack in that order, and then
# pops them off the stack in reverse order, at each stage of the search
# iter_dfs() will always traverse the neighboring nodes in reverse order from
# highest-numbered to lowest-numbered.

one_node_iter_dfs_trav = [1]
two_nodes_iter_dfs_trav = [1, 2]
maze_2x2_iter_dfs_trav = [1, 3, 4, 2]
binary_tree_iter_dfs_trav = [1, 3, 7, 6, 2, 5, 4]
maze_3x3_iter_dfs_trav = [1, 2, 5, 8, 9, 6, 7, 4, 3]

def test_iter_dfs_adjmx():
    assert iter_dfs(one_node_adjmx, 1, adjmx_adj_nodes) == one_node_iter_dfs_trav
    assert iter_dfs(two_nodes_adjmx, 1, adjmx_adj_nodes) == two_nodes_iter_dfs_trav
    assert iter_dfs(maze_2x2_adjmx, 1, adjmx_adj_nodes) == maze_2x2_iter_dfs_trav
    assert iter_dfs(binary_tree_adjmx, 1, adjmx_adj_nodes) == binary_tree_iter_dfs_trav
    assert iter_dfs(maze_3x3_adjmx, 1, adjmx_adj_nodes) == maze_3x3_iter_dfs_trav

def test_iter_dfs_adjl():
    assert iter_dfs(one_node_adjl, 1, adjl_adj_nodes) == one_node_iter_dfs_trav
    assert iter_dfs(two_nodes_adjl, 1, adjl_adj_nodes) == two_nodes_iter_dfs_trav
    assert iter_dfs(maze_2x2_adjl, 1, adjl_adj_nodes) == maze_2x2_iter_dfs_trav
    assert iter_dfs(binary_tree_adjl, 1, adjl_adj_nodes) == binary_tree_iter_dfs_trav
    assert iter_dfs(maze_3x3_adjl, 1, adjl_adj_nodes) == maze_3x3_iter_dfs_trav

def test_iter_dfs_edgl():
    assert iter_dfs(one_node_edgl, 1, edgl_adj_nodes) == one_node_iter_dfs_trav
    assert iter_dfs(two_nodes_edgl, 1, edgl_adj_nodes) == two_nodes_iter_dfs_trav
    assert iter_dfs(maze_2x2_edgl, 1, edgl_adj_nodes) == maze_2x2_iter_dfs_trav
    assert iter_dfs(binary_tree_edgl, 1, edgl_adj_nodes) == binary_tree_iter_dfs_trav
    assert iter_dfs(maze_3x3_edgl, 1, edgl_adj_nodes) == maze_3x3_iter_dfs_trav

def test_iter_dfs_incmx():
    assert iter_dfs(one_node_incmx, 1, incmx_adj_nodes) == one_node_iter_dfs_trav
    assert iter_dfs(two_nodes_incmx, 1, incmx_adj_nodes) == two_nodes_iter_dfs_trav
    assert iter_dfs(maze_2x2_incmx, 1, incmx_adj_nodes) == maze_2x2_iter_dfs_trav
    assert iter_dfs(binary_tree_incmx, 1, incmx_adj_nodes) == binary_tree_iter_dfs_trav
    assert iter_dfs(maze_3x3_incmx, 1, incmx_adj_nodes) == maze_3x3_iter_dfs_trav

def test_iter_dfs_adjmap():
    assert iter_dfs(one_node_adjmap, 1, adjmap_adj_nodes) == one_node_iter_dfs_trav
    assert iter_dfs(two_nodes_adjmap, 1, adjmap_adj_nodes) == two_nodes_iter_dfs_trav
    assert iter_dfs(maze_2x2_adjmap, 1, adjmap_adj_nodes) == maze_2x2_iter_dfs_trav
    assert iter_dfs(binary_tree_adjmap, 1, adjmap_adj_nodes) == binary_tree_iter_dfs_trav
    assert iter_dfs(maze_3x3_adjmap, 1, adjmap_adj_nodes) == maze_3x3_iter_dfs_trav

one_node_recurse_dfs_trav = [1]
two_nodes_recurse_dfs_trav = [1, 2]
maze_2x2_recurse_dfs_trav = [1, 2, 3, 4]
binary_tree_recurse_dfs_trav = [1, 2, 4, 5, 3, 6, 7]
maze_3x3_recurse_dfs_trav = [1, 2, 3, 5, 6, 9, 8, 7, 4]

def test_recurse_dfs_adjmx():
    assert recurse_dfs(one_node_adjmx, 1, adjmx_adj_nodes) == one_node_recurse_dfs_trav
    assert recurse_dfs(two_nodes_adjmx, 1, adjmx_adj_nodes) == two_nodes_recurse_dfs_trav
    assert recurse_dfs(maze_2x2_adjmx, 1, adjmx_adj_nodes) == maze_2x2_recurse_dfs_trav
    assert recurse_dfs(binary_tree_adjmx, 1, adjmx_adj_nodes) == binary_tree_recurse_dfs_trav
    assert recurse_dfs(maze_3x3_adjmx, 1, adjmx_adj_nodes) == maze_3x3_recurse_dfs_trav

def test_recurse_dfs_adjl():
    assert recurse_dfs(one_node_adjl, 1, adjl_adj_nodes) == one_node_recurse_dfs_trav
    assert recurse_dfs(two_nodes_adjl, 1, adjl_adj_nodes) == two_nodes_recurse_dfs_trav
    assert recurse_dfs(maze_2x2_adjl, 1, adjl_adj_nodes) == maze_2x2_recurse_dfs_trav
    assert recurse_dfs(binary_tree_adjl, 1, adjl_adj_nodes) == binary_tree_recurse_dfs_trav
    assert recurse_dfs(maze_3x3_adjl, 1, adjl_adj_nodes) == maze_3x3_recurse_dfs_trav

def test_recurse_dfs_edgl():
    assert recurse_dfs(one_node_edgl, 1, edgl_adj_nodes) == one_node_recurse_dfs_trav
    assert recurse_dfs(two_nodes_edgl, 1, edgl_adj_nodes) == two_nodes_recurse_dfs_trav
    assert recurse_dfs(maze_2x2_edgl, 1, edgl_adj_nodes) == maze_2x2_recurse_dfs_trav
    assert recurse_dfs(binary_tree_edgl, 1, edgl_adj_nodes) == binary_tree_recurse_dfs_trav
    assert recurse_dfs(maze_3x3_edgl, 1, edgl_adj_nodes) == maze_3x3_recurse_dfs_trav

def test_recurse_dfs_incmx():
    assert recurse_dfs(one_node_incmx, 1, incmx_adj_nodes) == one_node_recurse_dfs_trav
    assert recurse_dfs(two_nodes_incmx, 1, incmx_adj_nodes) == two_nodes_recurse_dfs_trav
    assert recurse_dfs(maze_2x2_incmx, 1, incmx_adj_nodes) == maze_2x2_recurse_dfs_trav
    assert recurse_dfs(binary_tree_incmx, 1, incmx_adj_nodes) == binary_tree_recurse_dfs_trav
    assert recurse_dfs(maze_3x3_incmx, 1, incmx_adj_nodes) == maze_3x3_recurse_dfs_trav

def test_recurse_dfs_adjmap():
    assert recurse_dfs(one_node_adjmap, 1, adjmap_adj_nodes) == one_node_recurse_dfs_trav
    assert recurse_dfs(two_nodes_adjmap, 1, adjmap_adj_nodes) == two_nodes_recurse_dfs_trav
    assert recurse_dfs(maze_2x2_adjmap, 1, adjmap_adj_nodes) == maze_2x2_recurse_dfs_trav
    assert recurse_dfs(binary_tree_adjmap, 1, adjmap_adj_nodes) == binary_tree_recurse_dfs_trav
    assert recurse_dfs(maze_3x3_adjmap, 1, adjmap_adj_nodes) == maze_3x3_recurse_dfs_trav



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
one_node_adjmap = [{}]


# ADJACENCY MATRIXES

# adjacency matrix
two_nodes_adjmx = [[inf, 1],
                  [1,   inf]]

# adjacency list
two_nodes_adjl = [[2],
                 [1]]

# edge list
two_nodes_edgl = [(1, 2)]

# incidence matrix
two_nodes_incmx = [[1],
                  [1]]

# adjacency map
two_nodes_adjmap = [{2: True},
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
maze_2x2_adjl = [[2, 3], # 1
                 [1],    # 2
                 [1, 4], # 3
                 [3]]    # 4

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
maze_2x2_incmx = [[1, 1, 0], # 1
                  [1, 0, 0], # 2
                  [0, 1, 1], # 3
                  [0, 0, 1]] # 4

# adjacency map
maze_2x2_adjmap = [{2: True, 3: True}, # 1
                   {1: True},          # 2
                   {1: True, 4: True}, # 3
                   {3: True}]          # 4


# BINARY TREE
#
# incidence matrix
#            1
#          /   \
#        2       3
#       / \     / \
#      4   5   6   7

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
binary_tree_adjl = [[2, 3],    # 1
                    [1, 4, 5], # 2
                    [1, 6, 7], # 3
                    [2],       # 4
                    [2],       # 5
                    [3],       # 6
                    [3]]       # 7

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
binary_tree_adjmap = [{2: True, 3: True},          # 1
                      {1: True, 4: True, 5: True}, # 2
                      {1: True, 6: True, 7: True}, # 3
                      {2: True},                   # 4
                      {2: True},                   # 5
                      {3: True},                   # 6
                      {3: True}]                   # 7


# 3 X 3 MAZE
# 
# 1 - 2 - 3
#     |    
# 4   5 - 6
# |   |   |
# 7 - 8 - 9

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
maze_3x3_adjl = [[2],       # 1
                 [1, 3, 5], # 2
                 [2],       # 3
                 [7],       # 4
                 [2, 6, 8], # 5
                 [5, 9],    # 6
                 [4],       # 7
                 [5, 7, 9], # 8
                 [6, 8]]    # 9

# edge list
maze_3x3_edgl = [(1, 2),
                 (2, 3),
                 (2, 5),
                 (4, 7),
                 (5, 6),
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
maze_3x3_incmx = [[1, 0, 0, 0, 0, 0, 0, 0, 0], # 1
                  [1, 1, 1, 0, 0, 0, 0, 0, 0], # 2
                  [0, 1, 0, 0, 0, 0, 0, 0, 0], # 3
                  [0, 0, 0, 0, 1, 0, 0, 0, 0], # 4
                  [0, 0, 1, 1, 0, 1, 0, 0, 0], # 5
                  [0, 0, 0, 1, 0, 0, 1, 0, 0], # 6
                  [0, 0, 0, 0, 1, 0, 0, 1, 0], # 7
                  [0, 0, 0, 0, 0, 1, 0, 1, 1], # 8
                  [0, 0, 0, 0, 0, 0, 1, 0, 1]] # 9


# adjacency map
maze_3x3_adjmap = [{2: True},                   # 1
                   {1: True, 3: True, 5: True}, # 2
                   {2: True},                   # 3
                   {7: True},                   # 4
                   {2: True, 6: True, 8: True}, # 5
                   {5: True, 9: True},          # 6
                   {4: True},                   # 7
                   {5: True, 7: True, 9: True}, # 8
                   {6: True, 8: True}]          # 9
