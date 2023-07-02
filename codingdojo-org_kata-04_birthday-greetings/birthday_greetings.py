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

import abc
import csv
import datetime
import os.path
import pytz
import sqlite3
import sys


def main():
    if len(sys.argv) == 1:
        print("Please specify a csv file on the commandline.")
        exit(1)
    elif len(sys.argv) > 2:
        print("Please specify only one file on the commandline.")
        exit(1)
    filename = sys.argv[1]
    if not filename.lower().endswith(".csv"):
        print("Please specify a csv file on the commandline.")
        exit(1)
    elif not os.path.exists(filename):
        print(f"File {filename} does not exist.")
        exit(1)

    csv_loader = Csv_Loader(filename)

    mail_sender = Mail_Sender("Fahey", "Kerne", "kernefahey@protonmail.com")

    send_msgs_w_loader_and_sender(csv_loader, mail_sender)


def send_msgs_w_loader_and_sender(loader_obj, sender_obj):
    friends_list = Friends_List()
    friends_list.add_from_loader(loader_obj)

    bday_today_friends = friends_list.friends_w_birthday_today()

    bday_msgs = [sender_obj.gen_bday_msg(friend_obj) for friend_obj in bday_today_friends]

    for bday_msg in bday_msgs:
        sender_obj.send_message(bday_msg)


class Data_Loader(metaclass=abc.ABCMeta):

    columns = "last_name", "first_name", "date_of_birth", "email", "phone_number"

    @abc.abstractmethod
    def __init__(self):
        pass


class Csv_Loader(Data_Loader):
    __slots__ = "rows",

    def __init__(self, filename):
        with open(filename, "r") as bdays_fh:
            birthday_file_rows = list(bdays_fh)
        reader = csv.reader(birthday_file_rows, quotechar='"', delimiter=',', skipinitialspace=True,
                                                     lineterminator='\n', quoting=csv.QUOTE_MINIMAL, doublequote=True)
        reader_iter = iter(reader)
        next(reader_iter)
        self.rows = [dict(zip(self.columns, row)) for row in reader_iter]
        for row_d in self.rows:
            row_d["date_of_birth"] = datetime.date(*map(int, row_d["date_of_birth"].split('/')))

    def __iter__(self):
        return iter(self.rows)


class Sqlite_Loader(Data_Loader):
    __slots__ = "connection", "cursor", "rows"

    def __init__(self, filename):
        self.connection = sqlite3.connect(filename)
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT " + ", ".join(self.columns) + " FROM birthdays;")
        self.rows = [dict(zip(self.columns, row)) for row in self.cursor]
        for row_d in self.rows:
            row_d["date_of_birth"] = datetime.date(*map(int, row_d["date_of_birth"].split('-')))

    def __iter__(self):
        return iter(self.rows)


class Friends_List:
    __slots__ = "_friend_objs",

    def __init__(self):
        self._friend_objs = list()

    def add_from_loader(self, loader_obj):
        for friend_d in loader_obj:
            self.add_friend(friend_d)

    def add_friend(self, friend_d):
        self._friend_objs.append(Friend(**friend_d))

    def __iter__(self):
        for friend_obj in self._friend_objs:
            yield friend_obj

    def friends_w_birthday_today(self):
        retval = list()
        todays_date = datetime.date.today()
        for friend_obj in self._friend_objs:
            if friend_obj.date_of_birth.day == todays_date.day and friend_obj.date_of_birth.month == todays_date.month:
                retval.append(friend_obj)
        return retval


class Friend:
    __slots__ = "last_name", "first_name", "date_of_birth", "email", "phone_number"

    def __init__(self, last_name, first_name, date_of_birth, email, phone_number):
        if not isinstance(date_of_birth, datetime.date):
            raise ValueError("date_of_birth argument to Friend constructor must be a datetime.date object")
        self.last_name = last_name
        self.first_name = first_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.phone_number = phone_number

    def __repr__(self):
        return "Friend({args})".format(args=", ".join(map(repr, (self.last_name, self.first_name, self.date_of_birth,
                                                                 self.email, self.phone_number))))


class Message(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def message_body(self):
        pass


class SMS_Message(Message):
    __slots__ = "from_number", "to_number", "message_body"

    def __init__(self, from_number, to_number, message_body):
        self.from_number = from_number
        self.to_number = to_number
        self.message_body = message_body

    def __repr__(self):
        return f"SMS_Message({repr(self.from_number)}, {repr(self.to_number)}, {repr(self.message_body)})"


class Mail_Message(Message):
    __slots__ = "from_line", "to_line", "date_line", "subject_line", "message_body"

    def __init__(self, from_line, date_line, to_line, subject_line, message_body):
        self.from_line = from_line
        self.to_line = to_line
        self.date_line = date_line
        self.subject_line = subject_line
        self.message_body = message_body

    def __repr__(self):
        return "Mail_Message({args})".format(args=", ".join(map(repr, (self.from_line, self.date_line, self.to_line,
                                                                       self.subject_line, self.message_body))))


class Message_Sender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def gen_bday_msg(self, friend_obj):
        pass

    @abc.abstractmethod
    def send_message(self, message_obj):
        pass


class Mail_Sender(Message_Sender):
    __slots__ = "from_last_name", "from_first_name", "from_address"

    def __init__(self, from_last_name, from_first_name, from_address):
        self.from_last_name = from_last_name
        self.from_first_name = from_first_name
        self.from_address = from_address

    def gen_bday_msg(self, friend_obj):
        timezone = pytz.timezone('America/Los_Angeles')
        todays_dt = datetime.datetime.now(timezone)

        from_line = f"From: {self.from_first_name} {self.from_last_name} <{self.from_address}>"
        date_line = todays_dt.strftime("Date: %-m/%-d/%y %-I:%M (GMT%z)")
        to_line = f"To: {friend_obj.first_name} {friend_obj.last_name} <{friend_obj.email}>"
        subject_line = "Subject: Happy Birthday!"
        message_body = f"Happy birthday, {friend_obj.first_name}!\n"

        return Mail_Message(from_line, date_line, to_line, subject_line, message_body)

    def send_message(self, message_obj):
        print(f"Sending mail message {repr(message_obj)}.")


class SMS_Sender(Message_Sender):
    __slots__ = "from_number",

    def __init__(self, from_number):
        self.from_number = from_number

    def gen_bday_msg(self, friend_obj):
        from_number = self.from_number
        to_number = friend_obj.phone_number
        message_body = f"Happy birthday, {friend_obj.first_name}!\n"

        return SMS_Message(from_number, to_number, message_body)

    def send_message(self, message_obj):
        print(f"Sending SMS message {repr(message_obj)}.")



if __name__ == "__main__":
    main()
