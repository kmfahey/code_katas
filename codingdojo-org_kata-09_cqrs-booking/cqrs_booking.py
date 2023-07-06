#!/usr/bin/python3

import attr

from datetime import date, timedelta


__all__ = "Room", "Booking", "Bookings_Register"


# Making the Room class immutable so objects of it can be used as dict keys.
# Doesn't seem to have any other applications and is arguably surplus to
# requirements. But it was in the instructions so I included it. Probably of
# more use in other languages that the author of this kata was thinking in when
# they wrote it.

@attr.s(frozen=True)
class Room:
    @staticmethod
    def _room_number_validator(self, attribute, room_number):
        if room_number < 100:
            raise ValueError("value for room_number must be 100 or greater")
        # The tallest hotel yet built is the Gevora hotel in the UAE, which has
        # 75 floors. 100 floors (times up to 100 rooms per floor) seems like a
        # reasonable maximum for room_number.
        elif room_number > 10099:
            raise ValueError("value for room_number must be less than 10099")

    room_number = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int), _room_number_validator))


# Making the Booking class immutable so sets can be used with it.
@attr.s(frozen=True)
class Booking:
    @staticmethod
    def _client_id_validator(self, attribute, client_id):
        if client_id < 0:
            raise ValueError("value for client_id must be greater than 0")
        # The maximum value the C data type unsigned long long can have on a
        # 64bit machine is 18446744073709551615. That seems like a reasonable
        # maximum for a client_id.
        elif client_id > 18446744073709551615:
            raise ValueError("value for client_id must be less than 18446744073709551616")

    @staticmethod
    def _date_validator(self, attribute, arrival_or_departure_date):
        if arrival_or_departure_date < date.today():
            raise ValueError(f"value for {attribute} must not be in the past")

    client_id = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int), _client_id_validator))
    room_number = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(int), Room._room_number_validator))
    arrival_date = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(date), _date_validator))
    departure_date = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of(date), _date_validator))

    def __init__(self, *argl):
       super().__init__(*argl)
       if self.departure_date < self.arrival_date:
           raise ValueError("value for departure_date must not be before value for arrival_date")

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

