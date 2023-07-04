#!/usr/bin/python3

from datetime import date

from dataclasses import dataclass


__all__ = "Room", "Booking", "Bookings_Register"


# Making the Room class immutable so objects of it can be used as dict keys.
# Doesn't seem to have any other applications and is arguably surplus to
# requirements. But it was in the instructions so I included it. Probably of
# more use in other languages that the author of this kata was thinking in when
# they wrote it.
@dataclass(frozen=True)
class Room:
    room_number: int


@dataclass
class Booking:
    client_id: int
    room_number: int
    arrival_date: date
    departure_date: date


class Bookings_Register:
    __slots__ = "rooms", "bookings"

    def __init__(self, rooms_per_floor=()):
        self.room_bookings = dict()
        for floor_number, rooms_on_this_floor in enumerate(rooms_per_floor, start=1):
            first_room_number = floor_number * 100
            last_room_number = 100 + rooms_on_this_floor - 1
            for room_number in range(first_room_number, last_room_number + 1):
                room_obj = Room(room_number)
                self.room_bookings[room_obj] = None

    def add_booking(self, room_number, client_id, arrival_date, departure_date):
        booking_obj = Booking(client_id, room_number, arrival_date, departure_date)
        self.bookings[Room(room_number)] = booking_obj

    def get_bookings(self, room_number):
        return self.bookings[Room(room_number)]

    def delete_booking(self, room_number):
        self.bookings[Room(room_number)] = None

    def get_booking(self, room_number):
        return self.bookings[Room(room_number)]
