#!/usr/bin/python3


from fizzbuzz import fizzbuzz


def test_fizzbuzz(mocker):
    expected_output = ["1\n", "2\n", "Fizz\n", "4\n", "Buzz\n", "Fizz\n", "7\n", "8\n", "Fizz\n", "Buzz\n", "11\n",
                       "Fizz\n", "13\n", "14\n", "FizzBuzz\n", "16\n", "17\n", "Fizz\n", "19\n", "Buzz\n"]
    output_lines = []
    mocker.patch("builtins.print", lambda *strings, sep=" ", end="\n": output_lines.append(str.join(sep, map(str, strings)) + end))
    fizzbuzz(1, 20)
    assert output_lines == expected_output
