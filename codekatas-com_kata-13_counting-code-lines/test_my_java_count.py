#!/usr/bin/python3


from my_java_count import count_lines_in_java_code


def test_1():
    assert count_lines_in_java_code("""foo;
bar;
baz;""") == 3


def test_2():
    assert count_lines_in_java_code("""foo;
bar; // baz
qux;""") == 3


def test_3():
    assert count_lines_in_java_code("""foo;
// bar
baz;""") == 2


def test_4():
    assert count_lines_in_java_code("""foo; /* bar */
baz;
qux;""") == 3


def test_5():
    assert count_lines_in_java_code("""foo;
/* bar */
baz;
qux;""") == 3


def test_6():
    assert count_lines_in_java_code("""/* foo */ bar;
baz;
qux;""") == 3

def test_7():
    assert count_lines_in_java_code("""/* foo */ bar; // baz
qux;
quux;""") == 3


def test_8():
    assert count_lines_in_java_code("""/* foo
bar
baz */
qux;
quux;
quuux;""") == 3


def test_9():
    assert count_lines_in_java_code("""/* foo
bar
baz */ qux;
quux;
quuux;""") == 3


def test_10():
    assert count_lines_in_java_code("""/* foo
bar
baz */ qux; // quux
quuux;
quuuux;""") == 3


if __name__ == "__main__":
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    test_9()
    test_10()
    print("all tests passed!")
