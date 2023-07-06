#!/usr/bin/python3

import pytest

from datetime import date, timedelta

from cqrs_booking import *


def test_room_class():
    room_obj = Room(117)
    assert room_obj.room_number == 117

def test_booking_class():
    today = date.today()
    tomorrow = today + timedelta(days=1)
    booking_obj = Booking(216, 117, today, tomorrow)
    assert booking_obj.client_id == 216
    assert booking_obj.room_number == 117
    assert booking_obj.arrival_date == today
    assert booking_obj.departure_date == tomorrow

def test_bookings_register_init():
    def get_max_room_on_floor(room_bookings, floor_number):
        room_number = floor_number * 100
        while Room(room_number + 1) in room_bookings:
            room_number += 1
        return room_number
    bookings_reg_obj = Bookings_Register((40, 40, 40, 40, 40))
    for floor_number in (1, 2, 3, 4, 5):
        assert get_max_room_on_floor(bookings_reg_obj.bookings, floor_number) % 100 == 39

def test_bookings_register_add_get_delete_booking_booked_rooms_free_rooms():
    today = date.today()
    tomorrow = today + timedelta(days=1)
    bookings_reg_obj = Bookings_Register((40, 40, 40, 40, 40))
    client_id = 216
    room_number = 117
    bookings_reg_obj.add_booking(client_id, room_number, today, tomorrow)
    assert room_number in bookings_reg_obj.get_booked_room_numbers()
    booking_obj = bookings_reg_obj.get_booking(room_number, today)
    assert booking_obj.client_id == client_id
    assert booking_obj.room_number == room_number
    assert booking_obj.arrival_date == today
    assert booking_obj.departure_date == tomorrow
    bookings_reg_obj.delete_booking(room_number, today)
    assert room_number in bookings_reg_obj.get_free_room_numbers()

def test_room_class_attr_usage():
    with pytest.raises(ValueError):
        room_obj = Room(-1)
    with pytest.raises(ValueError):
        room_obj = Room(65536)
    with pytest.raises(TypeError):
        room_obj = Room(3.14159)

def test_booking_class_attr_usage_client_id_attr():
    with pytest.raises(ValueError):
        booking_obj = Booking(-1, 144, date.today(), date.today() + timedelta(days=1))
    with pytest.raises(ValueError):
        booking_obj = Booking(2**65, 144, date.today(), date.today() + timedelta(days=1))
    with pytest.raises(TypeError):
        booking_obj = Booking(3.14159, 144, date.today(), date.today() + timedelta(days=1))

def test_booking_class_attr_usage_room_number_attr():
    with pytest.raises(ValueError):
        booking_obj = Booking(216, -1, date.today(), date.today() + timedelta(days=1))
    with pytest.raises(ValueError):
        booking_obj = Booking(216, 2**65, date.today(), date.today() + timedelta(days=1))
    with pytest.raises(TypeError):
        booking_obj = Booking(216, 3.14159, date.today(), date.today() + timedelta(days=1))

def test_booking_class_attr_usage_arrival_date_attr():
    with pytest.raises(ValueError):
        booking_obj = Booking(216, 144, date.today() - timedelta(days=1), date.today() + timedelta(days=1))
    with pytest.raises(TypeError):
        booking_obj = Booking(216, 144, date.today().strftime("%-m/%-d/$y"), date.today() + timedelta(days=1))

def test_booking_class_attr_usage_departure_date_attr():
    with pytest.raises(ValueError):
        booking_obj = Booking(216, 144, date.today(), date.today() - timedelta(days=1))
    with pytest.raises(TypeError):
        booking_obj = Booking(216, 144, date.today(), date.today().strftime("%-m/%-d/$y"))
