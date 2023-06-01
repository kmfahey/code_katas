#!/usr/bin/python3

import sys
import re


__all__ = ["count_lines_in_java_code"]


# N.B. I opted not to include a feature where a comment token that occurred
# inside a quoted string would not be processed. Implementing that would require
# parsing source code using regular expressions, which is well-known to be a
# fruitless endeavor.


def main():
    # Loading files from arguments.
    files = sys.argv[1:]

    test_files_list(files)

    # Iterates over the file list, loading the code from each one and testing
    # it.
    for java_file in files:
        with open(java_file, "r") as java_fh:
            line_count = count_lines_in_java_code(java_fh.read())
        print(f"file {java_file}: {line_count}")


# Checks commandline arguments.
def test_files_list(files):
    if not len(files):
        print("No java files supplied as arguments on the command line. Nothing to do.")
        exit(0)

    for file in files:
        if not file.endswith(".java"):
            print(f"Non-java-file argument {file} supplied as a command line argument. "
                  "Please only specify java code files as arguments.")


# Counts lines in the java code.
def count_lines_in_java_code(java_code):
    java_lines = java_code.split("\n")
    line_count = 0
    index = 0

    # For each potential line of code, this loop removes every possible
    # combination of comment from the line. and then checks if the line has any
    # non-space chars. If so, it's counted.
    #
    # If it initiated a multi-line comment, successive lines are discarded until
    # a multi-line comment closer is encountered. The end line is sent to the
    # next iteration to be checked in the same way.
    while index < len(java_lines):
        java_line = java_lines[index].strip()

        # Strips out any single-line comment.
        if '//' in java_line:
            java_line = re.sub(r'//.*$', '', java_line)

        # If a multi-line comment initiator token is found, strips out any
        # single-line version of it.
        if '/*' in java_line:
            java_line = re.sub(r'/\*.*?\*/', '', java_line)

        # If a multi-line comment closer is found, strips out any multi-line
        # comment conclusion.
        if '*/' in java_line:
            java_line = re.sub(r'^.*?\*/', '', java_line)

        # If there's still a multi-line comment initiator token in the line,
        # the remainder of the line is stripped out, then if it's nonempty and
        # nonwhitespace the line is counted. Then successive lines are discarded
        # until the multi-line comment closer is found. Then that line is sent
        # to the next iteration.
        if '/*' in java_line:
            java_line = re.sub(r'/\*.*$', '', java_line)
            if len(java_line) and not java_line.isspace():
                line_count += 1
            while '*/' not in java_line and index < len(java_lines):
                index += 1
                java_line = java_lines[index]
            continue

        # With all comment permutations having been checked for and
        # stripped out, the remaining line is checked. If it's nonempty and
        # nonwhitespace, it's counted.
        if len(java_line) and not java_line.isspace():
            line_count += 1
        index += 1
        continue

    return line_count


if __name__ == "__main__":
    main()
