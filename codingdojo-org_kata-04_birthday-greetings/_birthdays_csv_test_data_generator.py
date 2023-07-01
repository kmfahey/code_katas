#!/usr/bin/python3

import faker
import datetime
import operator

from test_birthday_greetings import generate_testing_data


table = generate_testing_data()

for row in table:
    print(*row, sep=", ")
