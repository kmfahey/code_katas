#!/usr/bin/python3

# Birthday Greetings
# 
# As you’re a very friendly person, you would like to send a birthday note to
# all the friends you have. But you have a lot of friends and a bit lazy, it may
# take some times to write all the notes by hand.
# 
# The good news is that computers can do it automatically for you.
# 
# Imagine you have a flat file with all your friends :
# 
# last_name, first_name, date_of_birth, email
# Doe, John, 1982/10/08, john.doe@foobar.com
# Ann, Mary, 1975/09/11, mary.ann@foobar.com
# 
# And you want to send them a happy birthday email on their birth date :
# 
# Subject: Happy birthday!
# 
# Happy birthday, dear <first_name>!
# 
# How would this software look like? Try to implement it so you can easily change :
# 
# * the way you retrieve the friends data (for instance, try switching to a
#   SQLite Db)
# * the way you send the note (for instance, imagine you want to send SMS
#   instead of emails)
# 
# What kind of tests would you write? Would you use Mocks?

import csv
import datetime


def instance_csv_reader(filename):
    with open(filename, "r") as bdays_fh:
        birthday_file_lines = list(bdays_fh)
    csv_reader = csv.reader(birthday_file_lines, quotechar='"', delimiter=',', skipinitialspace=True,
                                                 lineterminator='\n', quoting=csv.QUOTE_MINIMAL, doublequote=True)
    return csv_reader


def csv_to_friends(csv_reader):
    columns = next(csv_reader)
    friend_dicts_l = [dict(zip(columns, csv_line)) for csv_line in csv_reader]
    for friend_d in friend_dicts_l:
        friend_d["date_of_birth"] = datetime.date(*map(int, friend_d["date_of_birth"].split("/")))
    friend_objs = [Friend(**friend_d) for friend_d in friend_dicts_l]
    return friend_objs


class Friend:
    __slots__ = "last_name", "first_name", "date_of_birth", "email"

    def __init__(self, last_name, first_name, date_of_birth, email):
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.email = email

    def __repr__(self):
        return (f"Friend({repr(self.last_name)}, {repr(self.first_name)}, "
                        "{repr(self.date_of_birth)}, {repr(self.email)})")

    def gen_bday_msg(self):
        return f"Subject: Happy birthday!\nHappy birthday, dear {self.first_name}!\n"


class Birthday_Manager:
    __slots__ = "friend_objs",

    def __init__(self, friend_objs):
        self.friend_objs = dict()
        for friend_obj in friend_objs:
            if friend_obj.date_of_birth not in self.friend_objs:
                self.friend_objs[friend_obj.date_of_birth] = list()
                self.friend_objs[friend_obj.date_of_birth].append(friend_obj)
