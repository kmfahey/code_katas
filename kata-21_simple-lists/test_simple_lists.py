#!/usr/bin/python3


from simple_lists import Singly_Linked_List, Doubly_Linked_List, Dict_Based_List


def test_singly_linked_list():
    _test_list_class(Singly_Linked_List)


def test_doubly_linked_list():
    _test_list_class(Doubly_Linked_List)


def test_dict_based_list():
    _test_list_class(Dict_Based_List)


def _test_list_class(List_Class):
    list_obj = List_Class()

    assert not list_obj.find("fred")

    list_obj.add("fred")

    assert list_obj.find("fred").value == "fred"

    assert not list_obj.find("wilma")

    list_obj.add("wilma")

    assert list_obj.find("fred").value == "fred"

    assert list_obj.find("wilma").value == "wilma"

    assert list_obj.values() == ["fred", "wilma"]

    list_obj = List_Class()

    list_obj.add("fred")
    list_obj.add("wilma")
    list_obj.add("betty")
    list_obj.add("barney")

    assert list_obj.values() == ["fred", "wilma", "betty", "barney"]

    list_obj.delete(list_obj.find("wilma"))

    assert list_obj.values() == ["fred", "betty", "barney"]

    list_obj.delete(list_obj.find("barney"))

    assert list_obj.values() == ["fred", "betty"]

    list_obj.delete(list_obj.find("fred"))

    assert list_obj.values() == ["betty"]

    list_obj.delete(list_obj.find("betty"))

    assert list_obj.values() == []

