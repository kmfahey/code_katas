#!/usr/bin/python3


def fizzbuzz(start=1, end=100):
    for index in range(start, end + 1):
        if (index % 3 == 0 or "3" in str(index)) and (index % 5 == 0 or "5" in str(index)):
            print("FizzBuzz")
        elif index % 3 == 0 or "3" in str(index):
            print("Fizz")
        elif index % 5 == 0 or "5" in str(index):
            print("Buzz")
        else:
            print(index)
