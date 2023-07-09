#!/usr/bin/python3

from collections import OrderedDict

from math import inf


__all__ = "dfs", "adjmx_adjacent_nodes", "adjl_adjacent_nodes", "edgl_adjacent_nodes", "incmx_adjacent_nodes", "adjmap_adjacent_nodes"

def adjmx_adjacent_nodes(graph, this_node):
    adjrow = graph[this_node - 1]
    other_nodes = list()
    for index in range(len(adjrow)):
        if adjrow[index] == 1:
            other_nodes.append(index + 1)
    return other_nodes

def adjl_adjacent_nodes(graph, this_node):
    index = this_node - 1
    return sorted(graph[index])

def edgl_adjacent_nodes(graph, this_node):
    other_nodes = list()
    for edge in graph:
        left_node, right_node = edge
        if left_node == this_node:
            other_nodes.append(right_node)
        elif right_node == this_node:
            other_nodes.append(left_node)
    return sorted(other_nodes)

def incmx_adjacent_nodes(graph, node):
    node_index = node - 1  # adjust for 0-indexing
    adjacent_nodes = []
    for edge_index in range(len(graph[node_index])):
        if graph[node_index][edge_index] == 1:  # If node is part of edge
            # find the adjacent node(s)
            for other_node_index in range(len(graph)):
                if other_node_index != node_index and graph[other_node_index][edge_index] == 1:
                    # Append node number, adjusting for 1-indexing
                    adjacent_nodes.append(other_node_index + 1)
    return adjacent_nodes

def adjmap_adjacent_nodes(graph, this_node):
    index = this_node - 1
    return sorted(graph[index].keys())

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
