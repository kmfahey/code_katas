#!/usr/bin/python

import re


def dict_replace(string, dictionary):
    if any(s := re.fullmatch(r"(.*\W.*)", key) for key in dictionary):
        errant_token = s.group(1)
        raise ValueError("$-bounded tokens must consist of alphabetic characters, numeric characters, "
                         f"and the underscore character (dictionary contains '{errant_token}')")
    tokens = set(re.findall(r"\$(\w+)\$", string))
    test_string = re.subn(r"\$(\w+)\$", "", string)[0]
    if "$" in test_string:
        if test_string.count('$') == 1:
            raise ValueError("odd numbered count of symbol '$' in string argument")
        else:
            faulty_token = test_string.split('$')[1]
            raise ValueError("$-bounded tokens must consist of alphabetic characters, numeric characters, "
                             f"and the underscore character (string contains '{faulty_token}')")
    for token in tokens:
        if token not in dictionary:
            raise RuntimeError(f"token {token} found in string not present in dictionary")
        string = re.subn(fr"\${token}\$", dictionary[token], string)[0]
    return string
