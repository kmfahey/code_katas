#!/usr/bin/python3


__all__ = ["dependencies_for"]


def main():
    adjacency_list = {
        'A': ['B', 'C'],
        'B': ['C', 'E'],
        'C': ['G'],
        'D': ['A', 'F'],
        'E': ['F'],
        'F': ['H']
    }

    display_dependencies(adjacency_list)

    print()

    display_dependencies({"A": ["B"], "B": ["C"], "C": ["A"]})


# Displays the dependencies for all nodes in the adjacency list.
def display_dependencies(adjacency_list):
    for node in adjacency_list:
        dependencies = dependencies_for(adjacency_list, node)
        print(f"for node {node}, full dependency list is: " + ", ".join(dependencies))


# Returns the list of all dependencies for a given node in the given adjacency
# list.
def dependencies_for(adjacency_list, node):
    deps_set = set()
    add_dependencies_to_set(node, deps_set, adjacency_list)
    deps_set.remove(node)
    return list(sorted(deps_set))


# A recursive function that executes a depth-first search of the directed graph
# that is the adjacency list, populating a set of visited nodes, deps_set, as it
# goes.
def add_dependencies_to_set(node, deps_set, adjacency_list):
    deps_set.add(node)

    if node not in adjacency_list:
        return

    for neighbor in adjacency_list[node]:
        if neighbor in deps_set:
            continue
        add_dependencies_to_set(neighbor, deps_set, adjacency_list)


if __name__ == "__main__":
    main()


# Q&A
#
# "Does [the algorithm when presented with a circular dependency] work
# correctly? If not, ask yourself is this is a condition you should have
# considered during testing."
#
# Yes, it does.
#
#
# "Once you’ve got your code working with all the various test cases you can
# imagine, let’s think for a minute about performance. Say we were using this
# code to find all the relationships between the inhabitants of the United
# Kingdom. How would your code perform with 55-60 million items?"
#
# The only way to know how to find out would be to run it with 55-60 million
# items. As it happens I don't have enough RAM on my laptop to host a python
# interpreter that is handling data structures with tens of millions of
# elements. So I have no way of knowing.

