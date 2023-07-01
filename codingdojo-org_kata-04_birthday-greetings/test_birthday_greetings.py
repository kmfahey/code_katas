#!/usr/bin/python3

import datetime
import faker
import mock
import os
import os.path
import re
import tempfile

from birthday_greetings import Mail_Sender, Csv_Loader, Mail_Message, send_msgs_w_loader_and_sender


# Generates random birthday data until the table contains 3 rows with the
# same month and day as the system current date. Chooses name and birthday at
# random using faker. Typically generates between 200 and 4000 rows.
def generate_testing_data():
    faker_obj = faker.Faker()
    table = list()
    today = datetime.date.today()
    while 3 > sum(date_of_birth.month == today.month and date_of_birth.day == today.day
                  for _, __, date_of_birth, ___ in table):
        last_name = faker_obj.last_name()
        first_name = faker_obj.first_name()
        date_of_birth = faker_obj.date_between_dates(datetime.date(1990,1,1), datetime.date(2022,12,31))
        email = f"{first_name.lower()}.{last_name.lower()}@example.org"
        table.append([last_name, first_name, date_of_birth, email])
    for row in table:
        row[2] = row[2].strftime("%Y/%m/%d")
    table.insert(0, ["last_name", "first_name", "date_of_birth", "email"])
    return table


def test_send_msgs_w_loader_and_sender(mocker):
    faker_obj = faker.Faker()
    _, tempfile_name = tempfile.mkstemp(suffix=".csv")
    try:
        with open(tempfile_name, "w") as tempfile_obj:
            for row in generate_testing_data():
                print(*row, sep=", ", file=tempfile_obj)

        with open(tempfile_name, "r") as tempfile_obj:
            loader_obj = Csv_Loader(tempfile_name)

            test_last_name = faker_obj.last_name()
            test_first_name = faker_obj.first_name()
            test_email = f"{test_first_name.lower()}.{test_last_name.lower()}@example.org"
            sender_obj = Mail_Sender(test_last_name, test_first_name, test_email)

            message_objs_sent = list()

            def test_send_message(self, message_obj):
                message_objs_sent.append(message_obj)

            mocker.patch("birthday_greetings.Mail_Sender.send_message", test_send_message)

            send_msgs_w_loader_and_sender(loader_obj, sender_obj)

            assert len(message_objs_sent) == 3 and all(isinstance(obj, Mail_Message) for obj in message_objs_sent)
            assert all(re.match(r"^From: \w+ \w+ <\w+\.\w+@example.org>$", message_obj.from_line)
                       for message_obj in message_objs_sent)
            assert all(re.match(r"^Date: \d+/\d+/\d+ \d+:\d+ \([^)]+\)$", message_obj.date_line)
                       for message_obj in message_objs_sent)
            assert all(re.match(r"^To: \w+ \w+ <\w+\.\w+@example.org>$", message_obj.to_line)
                       for message_obj in message_objs_sent)
            assert all(message_obj.subject_line == "Subject: Happy Birthday!" for message_obj in message_objs_sent)
            assert all(re.match(r"Happy birthday, \w+!\n", message_obj.message_body) for message_obj in message_objs_sent)
    finally:
        os.unlink(tempfile_name)
