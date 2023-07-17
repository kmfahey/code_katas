#!/usr/bin/python3


def fizzbuzz(start=1, end=100):
    for index in range(start, end + 1):
        match (index % 3, index % 5):
            case (0, 0):
                print("FizzBuzz")
            case (0, _):
                print("Fizz")
            case (_, 0):
                print("Buzz")
            case _:
                print(index)
