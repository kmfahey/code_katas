#!/usr/bin/python3

from datetime import date

from dataclasses import dataclass


# Making the Room class immutable so objects of it can be used as dict keys,
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

#    def add_booking(self, booking_data):
#        # Command: Modifies the state (adds a booking)
#        # ...
#
#    def get_bookings(self, query_parameters):
#        # Query: Retrieves information (returns bookings)
#        # ...
#
#    def delete_booking(self, booking_id):
#        # Command: Modifies the state (deletes a booking)
#        # ...
#
#    def get_booking_details(self, booking_id):
#        # Query: Retrieves information (returns details of a booking)
#        # ...
