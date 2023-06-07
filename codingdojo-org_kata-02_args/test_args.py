#!/usr/bin/python3

from args import *


def test_par_like_cl_flags():
    cl_parser = CLArg_Parser(nonflag_allowed=False)
    cl_parser.add_flag("q", bool)
    cl_parser.add_flag("s", int)
    cl_parser.add_flag("w", int)
    assert sorted(cl_parser.get_flags()) == ["q", "s", "w"]
    cl_parser.parse(["-qs0w78"])
    assert cl_parser.get_flag_val("q") is True
    assert cl_parser.get_flag_val("s") == 0
    assert cl_parser.get_flag_val("w") == 78


if __name__ == "__main__":
    test_par_like_cl_flags()
