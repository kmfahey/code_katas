#!/usr/bin/python3


from fizzbuzz import fizzbuzz


def test_fizzbuzz(mocker):
    expected_output = ['1\n', '2\n', 'Fizz\n', '4\n', 'Buzz\n', 'Fizz\n', '7\n', '8\n', 'Fizz\n', 'Buzz\n', '11\n',
                       'Fizz\n', 'Fizz\n', '14\n', 'FizzBuzz\n', '16\n', '17\n', 'Fizz\n', '19\n', 'Buzz\n', 'Fizz\n',
                       '22\n', 'Fizz\n', 'Fizz\n', 'Buzz\n', '26\n', 'Fizz\n', '28\n', '29\n', 'FizzBuzz\n', 'Fizz\n',
                       'Fizz\n', 'Fizz\n', 'Fizz\n', 'FizzBuzz\n', 'Fizz\n', 'Fizz\n', 'Fizz\n', 'Fizz\n', 'Buzz\n',
                       '41\n', 'Fizz\n', 'Fizz\n', '44\n', 'FizzBuzz\n', '46\n', '47\n', 'Fizz\n', '49\n', 'Buzz\n']
    output_lines = []
    mocker.patch("builtins.print", lambda *strings, sep=" ", end="\n": output_lines.append(str.join(sep, map(str, strings)) + end))
    fizzbuzz(1, 50)
    assert output_lines == expected_output
