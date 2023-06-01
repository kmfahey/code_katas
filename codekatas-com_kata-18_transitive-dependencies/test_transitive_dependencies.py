#!/usr/bin/python3


from transitive_dependencies import dependencies_for


def test_dependencies_for():
    adjacency_list = {
        "A": ["B", "C"],
        "B": ["C", "E"],
        "C": ["G"],
        "D": ["A", "F"],
        "E": ["F"],
        "F": ["H"]
    }

    assert dependencies_for(adjacency_list, 'A') == ["B", "C", "E", "F", "G", "H"]
    assert dependencies_for(adjacency_list, 'B') == ["C", "E", "F", "G", "H"]
    assert dependencies_for(adjacency_list, 'C') == ["G"]
    assert dependencies_for(adjacency_list, 'D') == ["A", "B", "C", "E", "F", "G", "H"]
    assert dependencies_for(adjacency_list, 'E') == ["F", "H"]
    assert dependencies_for(adjacency_list, 'F') == ["H"]
