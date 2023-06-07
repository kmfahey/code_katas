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
    assert cl_parser.get_nonflag_args() is None

def test_other_flags():
    cl_parser = CLArg_Parser(nonflag_allowed=False)
    cl_parser.add_flag('B', int)
    cl_parser.add_flag('N', str)
    cl_parser.add_flag('x', float)
    cl_parser.add_flag('c', bool)
    cl_parser.add_flag('r', bool)
    argv = [arg.strip("'") for arg in "-B 1 -N 'foo' -x 0.5 -cr".split()]
    cl_parser.parse(argv)
    assert cl_parser.get_flag_val('B') == 1
    assert cl_parser.get_flag_val('N') ==  "foo"
    assert cl_parser.get_flag_val('x') == 0.5
    assert cl_parser.get_flag_val('c') == True
    assert cl_parser.get_flag_val('r') == True
    assert cl_parser.get_nonflag_args() is None

def test_flags_w_nonflag_args():
    cl_parser = CLArg_Parser(nonflag_allowed=True)
    cl_parser.add_flag('O', bool)
    cl_parser.add_flag('N', str)
    cl_parser.add_flag('F', bool)
    cl_parser.add_flag('I', float)
    cl_parser.add_flag('D', int)
    argv = [arg.strip("'") for arg in "-O -N 'foo' -F -I 0.5 -D 1 'foo' 'bar' 'baz'".split()]
    cl_parser.parse(argv)
    assert cl_parser.get_nonflag_args() == ["foo", "bar", "baz"]


if __name__ == "__main__":
    test_par_like_cl_flags()
    test_other_flags()
    test_flags_w_nonflag_args()
