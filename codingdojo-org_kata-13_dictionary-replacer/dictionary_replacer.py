#!/usr/bin/python

import re


def dict_replace(string, dictionary):
    tokens = set(re.findall(r"\$(\w+)\$", string))
    for token in tokens:
        if token not in dictionary:
            raise RuntimeError(f"token {token} found in string not present in dictionary")
        string = re.subn(fr"\${token}\$", dictionary[token], string)[0]
    return string
