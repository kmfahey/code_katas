#!/usr/bin/python3

import faker
import datetime
import operator


# Generates CSV file content in the format that birthday_greetings.py accepts as
# input. Chooses name and birthday at random using faker. Continues to generate
# rows until the accumulated rows contain 3 rows with the same month and day as
# the current date, then prints a header line and all rows in CSV format.
#
# Typically generates between 200 and 4000 rows.

faker_obj = faker.Faker()

table = list()

today = datetime.date.today()

while operator.lt(sum(date_of_birth.month == today.month and date_of_birth.day == today.day
                          for _, __, date_of_birth, ___ in table),
                  3):
    last_name = faker_obj.last_name()
    first_name = faker_obj.first_name()
    date_of_birth = faker_obj.date_between_dates(datetime.date(1990,1,1), datetime.date(2022,12,31))
    email = f"{first_name.lower()}.{last_name.lower()}@example.org"
    table.append([last_name, first_name, date_of_birth, email])

print("last_name, first_name, date_of_birth, email")

for last_name, first_name, date_of_birth, email in table:
    dob_str = date_of_birth.strftime("%Y/%m/%d")
    print(last_name, first_name, dob_str, email, sep=", ")
