#!/usr/bin/python3

from collections import OrderedDict

from math import inf


__all__ = "dfs", "adjmx_adj_nodes", "adjl_adj_nodes", "edgl_adj_nodes", "incmx_adj_nodes", "adjmap_adj_nodes"

def adjmx_adj_nodes(graph, this_node):
    adjrow = graph[this_node - 1]
    other_nodes = list()
    for index in range(len(adjrow)):
        if adjrow[index] == 1:
            other_nodes.append(index + 1)
    return other_nodes

def adjl_adj_nodes(graph, this_node):
    index = this_node - 1
    return sorted(graph[index])

def edgl_adj_nodes(graph, this_node):
    other_nodes = list()
    for edge in graph:
        left_node, right_node = edge
        if left_node == this_node:
            other_nodes.append(right_node)
        elif right_node == this_node:
            other_nodes.append(left_node)
    return sorted(other_nodes)

def incmx_adj_nodes(graph, node):
    node_index = node - 1  # adjust for 0-indexing
    adj_nodes = []
    for edge_index in range(len(graph[node_index])):
        if graph[node_index][edge_index] == 1:  # If node is part of edge
            # find the adjacent node(s)
            for other_node_index in range(len(graph)):
                if other_node_index != node_index and graph[other_node_index][edge_index] == 1:
                    # Append node number, adjusting for 1-indexing
                    adj_nodes.append(other_node_index + 1)
    return adj_nodes

def adjmap_adj_nodes(graph, this_node):
    index = this_node - 1
    return sorted(graph[index].keys())

# iterative
def dfs(graph, this_node, adj_nodes_func):
    stack = list()
    seen = OrderedDict()
    stack.append(this_node)
    while stack:
        this_node = stack.pop()
        if this_node not in seen:
            seen[this_node] = None
            for other_node in adj_nodes_func(graph, this_node):
                stack.append(other_node)
    return list(seen.keys())

# recursive (not yet functional)
# def recurs_dfs(graph, this_node, adj_nodes_func):
#     stack = list()
#     seen = OrderedDict()
#     def _dfs(node):
#         retval = [node]
#         seen[node] = True
#         for other_node in adj_nodes_func(graph, node):
#             if other_node not in seen:
#                 retval.extend(_dfs(other_node))
#         return sorted(retval, reverse=True)
#     return _dfs(this_node)
