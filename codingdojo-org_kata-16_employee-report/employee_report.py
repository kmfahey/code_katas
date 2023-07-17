#!/usr/bin/python3

import re
import attr


@attr.s(frozen=True)
class Employee:
    @staticmethod
    def _validate_name(value):
        if not re.match(r"^\s|\s$", value):
            raise ValueError("value for name must not begin or end with a space")
        elif not re.match(r"^([A-Za-zÀ-ÖØ-öø-ÿ '’ʼ-])+$", value):
            raise ValueError("value for name must contain only letters, spaces, apostrophes and dashes")

    @staticmethod
    def _validate_age(value):
        # Labor law in most states requires than workers be at least 16yo.
        if value < 16:
            raise ValueError("value for age must not be less than 16")
        # Sanity check. The oldest human to ever live died at 122. 125yo seems
        # like a reasonable maximum.
        elif value > 125:
            raise ValueError("value for age must not be greater than 125")

    name = attr.ib(type=str, validator=attr.validators.and_(attr.validators.instance_of(str), _validate_name))
    age = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of((int, float)), _validate_age))

    @property
    def can_work_sundays(self):
        return self.age >= 18


class Roster:
    __slots__ = "_employees",

    def __init__(self, employees):
        self._employees = list()
        self._employees.extend(employees)
