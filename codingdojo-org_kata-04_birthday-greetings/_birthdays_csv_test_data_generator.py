#!/usr/bin/python3

import sqlite3
import os.path

from test_birthday_greetings import generate_testing_data, prep_sqlite_loader_obj


table = generate_testing_data()

with open("birthdays2.csv", "w") as bday_fh:
    for row in table:
        print(*row, sep=", ", file=bday_fh)

print("birthdays2.csv created")

print(f"{len(table)-1} rows saved")

db_file_name = "birthdays2_sqlite.db"

prep_sqlite_loader_obj(db_file_name)

print("birthdays2_sqlite.db created & populated, or found & repopulated")

