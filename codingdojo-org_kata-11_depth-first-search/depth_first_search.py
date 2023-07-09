#!/usr/bin/python3

from collections import OrderedDict

from math import inf


def adjmx_adjacent_edges(graph, this_vertex):
    adjrow = graph[this_vertex - 1]
    other_vertexes = list()
    for index in range(len(adjrow)):
        if adjrow[index] == 1:
            other_vertexes.append(index + 1)
    return other_vertexes

def iter_depth_1st_search(graph, this_vertex):
    stack = list()
    seen = OrderedDict()
    stack.append(this_vertex)
    while stack:
        this_vertex = stack.pop()
        if this_vertex not in seen:
            seen[this_vertex] = None
            for other_vertex in adjmx_adjacent_edges(graph, this_vertex):
                stack.append(other_vertex)
    return list(seen.keys())
