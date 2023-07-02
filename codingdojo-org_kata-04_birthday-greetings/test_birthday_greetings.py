#!/usr/bin/python3

import datetime
import faker
import os
import os.path
import random
import re
import sqlite3
import tempfile

from birthday_greetings import Mail_Sender, Csv_Loader, Mail_Message, SMS_Message, Sqlite_Loader, send_msgs_w_loader_and_sender


# faker.Faker.phone_number() returns all kinds of phone numbers in different
# formats including ones with extensions. That's not the set of phone numbers
# that can receive SMS messages, so phoe number generation is done manually.
AREA_CODES = (
    201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 212, 213, 214, 215, 216, 217, 218, 219, 220, 223, 224, 225, 226,
    227, 228, 229, 231, 234, 236, 239, 240, 242, 246, 248, 249, 250, 251, 252, 253, 254, 256, 260, 262, 263, 264, 267,
    268, 269, 270, 272, 274, 276, 279, 281, 283, 284, 289, 301, 302, 303, 304, 305, 306, 307, 308, 309, 310, 312, 313,
    314, 315, 316, 317, 318, 319, 320, 321, 323, 325, 326, 329, 330, 331, 332, 334, 336, 337, 339, 340, 341, 343, 345,
    346, 347, 350, 351, 352, 354, 360, 361, 363, 364, 365, 367, 368, 369, 380, 382, 385, 386, 401, 402, 403, 404, 405,
    406, 407, 408, 409, 410, 412, 413, 414, 415, 416, 417, 418, 419, 423, 424, 425, 428, 430, 431, 432, 434, 435, 437,
    438, 440, 441, 442, 443, 445, 447, 448, 450, 458, 463, 464, 468, 469, 470, 472, 473, 474, 475, 478, 479, 480, 484,
    501, 502, 503, 504, 505, 506, 507, 508, 509, 510, 512, 513, 514, 515, 516, 517, 518, 519, 520, 530, 531, 534, 539,
    540, 541, 548, 551, 557, 559, 561, 562, 563, 564, 567, 570, 571, 572, 573, 574, 575, 579, 580, 581, 582, 584, 585,
    586, 587, 601, 602, 603, 604, 605, 606, 607, 608, 609, 610, 612, 613, 614, 615, 616, 617, 618, 619, 620, 623, 626,
    628, 629, 630, 631, 636, 639, 640, 641, 646, 647, 649, 650, 651, 656, 657, 658, 659, 660, 661, 662, 664, 667, 669,
    670, 671, 672, 678, 680, 681, 682, 683, 684, 689, 701, 702, 703, 704, 705, 706, 707, 708, 709, 712, 713, 714, 715,
    716, 717, 718, 719, 720, 721, 724, 725, 726, 727, 728, 731, 732, 734, 737, 740, 742, 743, 747, 753, 754, 757, 758,
    760, 762, 763, 765, 767, 769, 770, 771, 772, 773, 774, 775, 778, 779, 780, 781, 782, 784, 785, 786, 787, 801, 802,
    803, 804, 805, 806, 807, 808, 809, 810, 812, 813, 814, 815, 816, 817, 818, 819, 820, 825, 826, 828, 829, 830, 831,
    832, 835, 838, 839, 840, 843, 845, 847, 848, 849, 850, 854, 856, 857, 858, 859, 860, 861, 862, 863, 864, 865, 867,
    868, 869, 870, 872, 873, 876, 878, 901, 902, 903, 904, 905, 906, 907, 908, 909, 910, 912, 913, 914, 915, 916, 917,
    918, 919, 920, 925, 928, 929, 930, 931, 934, 936, 937, 938, 939, 940, 941, 943, 945, 947, 948, 949, 951, 952, 954,
    956, 959, 970, 971, 972, 973, 978, 979, 980, 983, 984, 985, 986, 989, 500, 521, 522, 523, 524, 525, 526, 527, 528,
    529, 533, 544, 566, 577, 588, 600, 622, 633, 700, 710, 800, 833, 844, 855, 866, 877, 888, 900)


# Generates random birthday data until the table contains 3 rows with the
# same month and day as the system current date. Chooses name and birthday at
# random using faker. Typically generates between 200 and 4000 rows.
def generate_testing_data(w_header=True):
    faker_obj = faker.Faker()
    table = list()
    today = datetime.date.today()
    # Continues to generate new random identity quintuples and store them to table until table
    # contains three identity quintuples where today is their birthday.
    while sum(row[2].month == today.month and row[2].day == today.day for row in table) < 3:
        last_name = faker_obj.last_name()
        first_name = faker_obj.first_name()
        date_of_birth = faker_obj.date_between_dates(datetime.date(1990,1,1), datetime.date(2022,12,31))
        email = f"{first_name.lower()}.{last_name.lower()}@example.org"
        phone_number = "1 ({area_code}) {prefix}-{line_number}".format(
            area_code=str(random.choice(AREA_CODES)),
            prefix=str(random.randint(1, 999)).zfill(3),
            line_number=str(random.randint(1, 9999)).zfill(3))
        table.append([last_name, first_name, date_of_birth, email, phone_number])
    for row in table:
        row[2] = row[2].strftime("%Y/%m/%d")
    if w_header:
        table.insert(0, ["last_name", "first_name", "date_of_birth", "email", "phone_number"])
    return table


def test_send_msgs_csv_loader_mail_sender(mocker):
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
            assert all(re.match(r"Happy birthday, \w+!\n", message_obj.message_body)
                       for message_obj in message_objs_sent)
    finally:
        os.unlink(tempfile_name)


def test_send_msgs_sqlite_loader_mail_sender(mocker):
    faker_obj = faker.Faker()
    _, tempfile_name = tempfile.mkstemp(suffix=".db")
    try:
        tempfile_name = "birthdays2_sqlite.db"
        db_conx = sqlite3.connect(tempfile_name)
        db_curs = db_conx.cursor()
        db_curs.execute("""CREATE TABLE IF NOT EXISTS birthdays (
                                last_name VARCHAR(64),
                                first_name VARCHAR(64),
                                date_of_birth VARCHAR(10),
                                email VARCHAR(64),
                                phone_number VARCHAR(25)
                           );""")
        table = generate_testing_data(w_header=False)
        for last_name, first_name, date_of_birth, email, phone_number in table:
            year, month, day = date_of_birth.split('/')
            db_curs.execute(f"""INSERT INTO birthdays (last_name, first_name, date_of_birth, email, phone_number)
                                VALUES ('{last_name}', '{first_name}', '{year}-{month}-{day}', '{email}', '{phone_number}');""")
            db_conx.commit()
        loader_obj = Sqlite_Loader(tempfile_name)

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
        assert all(re.match(r"Happy birthday, \w+!\n", message_obj.message_body)
                   for message_obj in message_objs_sent)
    finally:
        os.unlink(tempfile_name)


