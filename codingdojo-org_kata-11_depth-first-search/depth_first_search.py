#!/usr/bin/python3

from collections import OrderedDict

from math import inf


__all__ = "dfs", "adjmx_adjacent_nodes"

def adjmx_adjacent_nodes(graph, this_node):
    adjrow = graph[this_node - 1]
    other_nodes = list()
    for index in range(len(adjrow)):
        if adjrow[index] == 1:
            other_nodes.append(index + 1)
    return other_nodes

def dfs(graph, this_node, adjacent_edges):
    stack = list()
    seen = OrderedDict()
    stack.append(this_node)
    while stack:
        this_node = stack.pop()
        if this_node not in seen:
            seen[this_node] = None
            for other_node in adjacent_edges(graph, this_node):
                stack.append(other_node)
    return list(seen.keys())
