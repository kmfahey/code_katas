#!/usr/bin/python3

from pytest import raises

from employee_report import Employee, Roster


master_roster_obj = Roster((Employee("Max", 17), Employee("Sepp", 18), Employee("Nina", 15), Employee("Mike", 51)))


def test_employee_init():
    with raises(ValueError):
        empl = Employee("John Doe", 13)
    with raises(ValueError):
        empl = Employee("John Doe", 190)
    with raises(ValueError):
        empl = Employee("John! Doe!", 25)
    with raises(ValueError):
        empl = Employee(" John Doe ", 25)
    empl = Employee("john doe", 25)
    assert empl.name == "John Doe"


def test_list_empl_sundays():
    roster_obj = master_roster_obj.copy()
    employees = roster_obj.list_empl()
    empl_can_work_sundays = roster_obj.list_empl(can_work_sundays=True)
    assert len(employees) != 0
    assert len(empl_can_work_sundays) != 0
    assert len(employees) >= len(empl_can_work_sundays)
    for employee in employees:
        if employee.age >= 18:
            assert any(employee == sunday_empl for sunday_empl in empl_can_work_sundays)
        else:
            assert not any(employee == sunday_empl for sunday_empl in empl_can_work_sundays)


def test_list_empl_sorted():
    roster_obj = master_roster_obj.copy()

    employees = roster_obj.list_empl()
    empl_sorted = roster_obj.list_empl(sorted_by_name=True)
    assert len(employees) != 0
    assert len(empl_sorted) != 0
    assert len(employees) == len(empl_sorted)
    for left_empl, right_empl in zip(empl_sorted, empl_sorted[1:]):
        assert left_empl.name <= right_empl.name

    empl_sorted_rev = roster_obj.list_empl(sorted_by_name=True, reverse=True)
    assert len(empl_sorted) != 0
    assert len(employees) == len(empl_sorted)
    for left_empl, right_empl in zip(empl_sorted_rev, empl_sorted_rev[1:]):
        assert left_empl.name >= right_empl.name


