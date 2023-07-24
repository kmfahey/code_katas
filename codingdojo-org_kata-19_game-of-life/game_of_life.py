#!/usr/bin/python3

import argparse
import attr
import os.path
import re
import select
import sys


__version__ = "0.1"

parser = argparse.ArgumentParser("titlecase")

parser.add_argument("-v", "--version", action="store_true", default=False, dest="show_version",
                    help="Display version information and exit.")

parser.add_argument("files", nargs=argparse.REMAINDER, help="Game of life snapshot files")


class ParsingError(Exception):
    pass


def main():
    options = parser.parse_args()

    if options.show_version:
        print(f"titlecase.py v.{__version__}. Author: K M Fahey. "
              "Placed in the public domain under The Unlicence <https://unlicense.org/>.")
        exit(0)

    input_blocks = get_input(options)

    snapshots = [parse_snapshot_file(input_block) for input_block in input_blocks]

    for snapshot in snapshots:
        snapshot.advance()
        print(str(snapshot))


def get_input(options):
    input_blocks = []
    if pending_on_stdin() and pending_on_argv(options):
        print("Data input by standard input while one or more files specified on the commandline. "
              "Cannot handle both inputs.")
        exit(1)
    elif pending_on_stdin():
        input_blocks.append(sys.stdin.read())
    elif pending_on_argv(options):
        for filename in options.files:
            if not os.path.exists(filename):
                print(f"Error in filename argument '{filename}': file does not exist.")
                exit(1)
            with open(filename, 'r') as gol_file:
                input_blocks.append(gol_file.read())
    else:
        print("No data pending on stdin and no file specified as an argument; nothing to do.")
        exit(1)
    return input_blocks


def pending_on_argv(options):
    return len(options.files)


def pending_on_stdin():
    return sys.stdin in select.select([sys.stdin],[],[],0.0)[0]


def parse_snapshot_file(snapshot_text):
    snapshot_lines = snapshot_text.strip().split("\n")

    generation_line = snapshot_lines.pop(0)
    generation_match = re.match(r"^Generation (\d+):$", generation_line)
    if generation_match is None:
        raise ParsingError("Could not parse generation from first line of input")
    generation = int(generation_match.group(1))

    dimensions_line = snapshot_lines.pop(0)
    dimensions_match = re.match(r"^(\d+) (\d+)$", dimensions_line)
    if dimensions_match is None:
        raise ParsingError("Could not parse dimensions from first line of input")
    x_dim, y_dim = map(int, dimensions_match.group(1, 2))

    if len(snapshot_lines) != y_dim:
        raise ParsingError("number of rows of cell grid not equal to declared vertical dimension")
    elif not all(len(snapshot_line) == x_dim for snapshot_line in snapshot_lines):
        raise ParsingError("some rows in cell grid not of the declared horizontal dimension")
    elif not all(snapshot_char in ('.', '*')
                 for snapshot_line in snapshot_lines
                 for snapshot_char in snapshot_line):
        raise ParsingError("some characters in cell grid rows are not either '.' or '*'")

    cellgrid = [[None] * x_dim for _ in range(y_dim)]

    for y_index in range(y_dim):
        for x_index in range(x_dim):
            cellgrid[y_index][x_index] = 1 if snapshot_lines[y_index][x_index] == '*' else 0

    return Game_of_Life_Snapshot(generation, x_dim, y_dim, cellgrid)


@attr.s
class Game_of_Life_Snapshot:
    @staticmethod
    def _validate_int_param(self, attribute, value):
        if value < 1:
            raise ValueError(f"value for {attribute} must be greater than or equal to 1")

    @staticmethod
    def _validate_cellgrid(self, attribute, value):
        if not isinstance(value, (tuple, list)):
            raise ValueError("value for cellgrid must be a list or tuple")
        elif not all(isinstance(elem, (list, tuple)) for elem in value):
            raise ValueError("every element of cellgrid must be a list or tuple")

    generation = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int),
                                                                  _validate_int_param))
    x_dim = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int),
                                                             _validate_int_param))
    y_dim = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int),
                                                             _validate_int_param))
    cellgrid = attr.ib(type=list, validator=attr.validators.and_(attr.validators.instance_of((list, tuple)),
                                                                 _validate_cellgrid))

    def __str__(self):
        retvals = [f"Generation {self.generation}:",
                   f"{self.x_dim} {self.y_dim}"]
        for cellgrid_row in self.cellgrid:
            retval_line = ""
            for elem in cellgrid_row:
                retval_line += "*" if elem else "."
            retvals.append(retval_line)
        return str.join("\n", retvals)

    def advance(self):
        new_cellgrid = [[None] * self.x_dim for _ in range(self.y_dim)]
        for y_index in range(self.y_dim):
            for x_index in range(self.x_dim):

# Less elegant but eminently more debuggable alternative algorithm
#
#                 adj_coords = [(x_index + x_mod, y_index + y_mod)
#                               for x_mod in range(-1, 2)
#                               for y_mod in range(-1, 2)]
#                 adj_coords = list(filter(lambda coord: coord[0] or coord[1], adj_coords))
#                 adj_coords = list(filter(lambda coord: 0 <= coord[0] < self.x_dim, adj_coords))
#                 adj_coords = list(filter(lambda coord: 0 <= coord[1] < self.y_dim, adj_coords))
#                 sum_of_neighbors = sum(self.cellgrid[adj_y_index][adj_x_index]
#                                        for adj_x_index, adj_y_index in adj_coords)
#                 new_cellgrid[y_index][x_index] = (1 if sum_of_neighbors == 3
#                                                     else self.cellgrid[y_index][x_index] if sum_of_neighbors == 2
#                                                     else 0)

                adj_coords = [(x_index + x_mod, y_index + y_mod)
                              for x_mod in range(-1, 2)
                                                           # Omits result that's simply the original coordinates.
                              for y_mod in range(-1, 2) if (x_mod or y_mod) and
                                                           # Omits results that fall outside the perimeter of the grid
                                                           0 <= x_index + x_mod < self.x_dim and
                                                           0 <= y_index + y_mod < self.y_dim]
                sum_of_neighbors = sum(self.cellgrid[adj_y_index][adj_x_index]
                                       for adj_x_index, adj_y_index in adj_coords)
                new_cellgrid[y_index][x_index] = (1 if sum_of_neighbors == 3
                                                    else self.cellgrid[y_index][x_index] if sum_of_neighbors == 2
                                                    else 0)
        self.cellgrid = new_cellgrid


if __name__ == "__main__":
    main()
