#!/usr/bin/python3

import re
import attr


__all__ = "Employee", "Roster"


@attr.s(frozen=True)
class Employee:
    @staticmethod
    def _validate_name(self, attribute, value):
        if re.match(r"^\s|\s$", value):
            raise ValueError("value for name must not begin or end with a space")
        elif not re.match(r"^([A-Za-zÀ-ÖØ-öø-ÿ '’ʼ-])+$", value):
            raise ValueError("value for name must contain only letters, spaces, apostrophes and dashes")

    @staticmethod
    def _validate_age(self, attribute, value):
        if value < 14:
            raise ValueError("value for age must not be less than 14")
        # Sanity check. The oldest human to ever live died at 122. 125yo seems
        # like a reasonable maximum.
        elif value > 125:
            raise ValueError("value for age must not be greater than 125")

    name = attr.ib(type=str, validator=attr.validators.and_(attr.validators.instance_of(str), _validate_name))
    age = attr.ib(type=int, validator=attr.validators.and_(attr.validators.instance_of((int, float)), _validate_age))

    @property
    def can_work_sundays(self):
        return self.age >= 18

    def __repr__(self):
        return f"Employee(name={repr(self.name)}, age={repr(self.age)})"


class Roster:
    __slots__ = "_employees",

    def __init__(self, employees):
        self._employees = list()
        self._employees.extend(employees)

    def copy(self):
        return Roster(self._employees.copy())

    def list_empl(self, can_work_sundays=False, sorted_by_name=False, reverse=False):
        empl_list = self._employees.copy()
        if can_work_sundays:
            empl_list = list(filter(lambda empl: empl.age >= 18, self.list_empl()))
        if sorted_by_name:
            empl_list = sorted(empl_list, key=lambda empl: empl.name, reverse=reverse)
        return empl_list
