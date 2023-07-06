#!/usr/bin/python3

from datetime import date, timedelta

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


# Making the Booking class immutable so sets can be used with it.
@dataclass(frozen=True)
class Booking:
    client_id: int
    room_number: int
    arrival_date: date
    departure_date: date

    # returns a list of every date between arrival_date and departure_date, inclusive
    def gen_dates_booked(self):
        duration = (self.departure_date - self.arrival_date).days
        retval = [self.arrival_date + timedelta(days=day_number) for day_number in range(0, duration)]
        return retval


# A class that encapsulates a data structure that associates Room objects with
# Booking objects in a calendar-aware fashion, presents methods for interacting
# with that data structure.
class Bookings_Register:
    __slots__ = "bookings",

    def __init__(self, rooms_per_floor=()):
        self.bookings = dict()
        for floor_number, rooms_on_this_floor in enumerate(rooms_per_floor, start=1):
            first_room_number = floor_number * 100
            last_room_number = first_room_number + rooms_on_this_floor - 1
            for room_number in range(first_room_number, last_room_number + 1):
                room_obj = Room(room_number)
                self.bookings[room_obj] = dict()

    # interprets arguments into a room object and a booking object. associates
    # that booking with that room for all dates between arrival_date and
    # departure_date.
    def add_booking(self, client_id, room_number, arrival_date, departure_date):
        room_obj = Room(room_number)
        booking_obj = Booking(client_id, room_number, arrival_date, departure_date)
        dates_booked = booking_obj.gen_dates_booked()
        for day_booked in dates_booked:
            self.bookings[room_obj][day_booked] = booking_obj

    # Accepts a room number and a day on which the room is booked. day_booked
    # can be any date between arrival_date and departure_date on the original
    # booking; it will be used to find the booking by seeking one where
    # day_booked falls between arrival and departure inclusive. Returns the
    # number of days freed up by the deletion. If no such booking was found
    # returns 0.
    def delete_booking(self, room_number, day_booked):
        room_obj = Room(room_number)
        booking_obj_to_del = None
        # Seeking a booking where day_booked falls between arrival_date and
        # depature_date inclusive
        for booking_obj in set(self.bookings[room_obj].values()):
            if booking_obj.arrival_date <= day_booked <= booking_obj.departure_date:
                booking_obj_to_del = booking_obj
                break
        if booking_obj_to_del is None:
            # No booking was found.
            return 0
        days_occupied = [day_occupied for day_occupied, booking_obj in self.bookings[room_obj].items()
                         if booking_obj is booking_obj_to_del]
        # Deletes every day between arrival_date and departure_date inclusive
        # from the room object's dict in the bookings data structure.
        for day_occupied in days_occupied:
            del self.bookings[room_obj][day_occupied]
        return len(days_occupied)

    # Finds the booking in the room object's place in the bookings data
    # structure where the day_of_interest falls between arrival_date and
    # departure_date inclusive.
    def get_booking(self, room_number, day_of_interest):
        room_obj = Room(room_number)
        if day_of_interest in self.bookings[room_obj]:
            return self.bookings[room_obj][day_of_interest]
        return None

    # Returns the room number of every room that is booked on the day of
    # interest.
    def get_booked_room_numbers(self, day_of_interest=date.today()):
        return [room_obj.room_number for room_obj in self.bookings if day_of_interest in self.bookings[room_obj]]

    # Returns the room number of every room that is open on the day of
    # interest.
    def get_free_room_numbers(self, day_of_interest=date.today()):
        return [room_obj.room_number for room_obj in self.bookings if day_of_interest not in self.bookings[room_obj]]

