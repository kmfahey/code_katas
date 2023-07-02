#!/usr/bin/python3

import sqlite3
import os.path

from test_birthday_greetings import generate_testing_data


table = generate_testing_data()

with open("birthdays2.csv", "w") as bday_fh:
    for row in table:
        print(*row, sep=", ", file=bday_fh)

print("birthdays2.csv created")

print(f"{len(table)-1} rows saved")

db_file_name = "birthdays2_sqlite.db"

if not os.path.exists(db_file_name):
    db_conx = sqlite3.connect(db_file_name)
    print(f"{db_file_name} created")
else:
    db_conx = sqlite3.connect(db_file_name)
    print(f"{db_file_name} connected to")

db_curs = db_conx.cursor()

result = db_curs.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='table_name';")

if not result:
    db_curs.execute("""CREATE TABLE IF NOT EXISTS birthdays (
                            last_name VARCHAR(64),
                            first_name VARCHAR(64),
                            date_of_birth VARCHAR(10),
                            email VARCHAR(64)
                       );""")
    print("table birthdays created")
else:
    result = db_curs.execute("DELETE FROM birthdays;")
    rows_deleted = result.rowcount
    print("birthdays table cleared")
    print(f"{rows_deleted} rows deleted")
    db_conx.commit()

table_iter = iter(table)

# skip the first row, which is the header row of the csv
next(table_iter)

for last_name, first_name, date_of_birth, email in table_iter:
    year, month, day = date_of_birth.split('/')
    db_curs.execute(f"""INSERT INTO birthdays (last_name, first_name, date_of_birth, email)
                        VALUES ('{last_name}', '{first_name}', '{year}-{month}-{day}', '{email}');""")
    db_conx.commit()

print(f"{len(table)-1} rows inserted into table `birthdays`")
