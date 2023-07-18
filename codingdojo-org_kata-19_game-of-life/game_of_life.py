#!/usr/bin/python3

import os.path
import sys
import select
import argparse


__version__ = "0.1"

parser = argparse.ArgumentParser("titlecase")

parser.add_argument("-v", "--version", action="store_true", default=False, dest="show_version",
                    help="Display version information and exit.")

parser.add_argument("files", nargs=argparse.REMAINDER, help="Game of life snapshot files")


def main():
    options = parser.parse_args()

    if options.show_version:
        print(f"titlecase.py v.{__version__}. Author: K M Fahey. "
              "Placed in the public domain under The Unlicence <https://unlicense.org/>.")
        exit(0)

    input_blocks = get_input(options)


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
