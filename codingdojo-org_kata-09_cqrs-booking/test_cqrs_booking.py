#!/usr/bin/python3

from datetime import date, timedelta

from cqrs_booking import *


def test_room_class():
    room_obj = Room(117)
    assert room_obj.room_number == 117

def test_booking_class():
    today = date.today()
    tomorrow = timedelta(days=1)
    booking_obj = Booking(216, 117, today, tomorrow)
    assert booking_obj.client_id == 216
    assert booking_obj.room_number == 117
    assert booking_obj.arrival_date == today
    assert booking_obj.departure_date == tomorrow

