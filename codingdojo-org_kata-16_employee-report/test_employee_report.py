#!/usr/bin/python3

from employee_report import Employee, Roster


master_roster_obj = Roster((Employee("Max", 17), Employee("Sepp", 18), Employee("Nina", 15), Employee("Mike", 51)))


def test_list_empl():
    roster_obj = master_roster_obj.copy()
    employees = set(roster_obj.list_empl())
    nonminors = set(roster_obj.nonminor_empl())
    for employee in employees:
        if employee.age >= 18:
            assert employee in nonminors
        else:
            assert employee not in nonminors
