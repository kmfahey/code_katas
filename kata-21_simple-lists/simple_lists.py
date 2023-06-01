#!/usr/bin/python3

import abc


__all__ = ["Singly_Linked_List", "Doubly_Linked_List", "Dict_Based_List"]


# Abstract superclass for the list implementations
class List_Impl(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def find(self, value):
        pass

    @abc.abstractmethod
    def add(self, value):
        pass

    @abc.abstractmethod
    def delete(self, element):
        pass

    @abc.abstractmethod
    def values(self):
        pass


# Abstract superclass for the list node implementations
class List_Node_Impl(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def element(self):
        pass


# Represents an element in the list. Is the payload of a node, and has the
# string value as its own payload.
class String_Element:
    __slots__ = "value",

    def __init__(self, value=None):
        self.value = value


# Singly-linked-list implementation. Every node has a reference to the next
# node.
class Singly_Linked_List(List_Impl):
    __slots__ = "head_node",

    def __init__(self):
        self.head_node = None

    # Searches the list for an element whose value attribute equals the value
    # argument. Returns that element if found, otherwise returns None.
    def find(self, value):
        cursor = self.head_node
        while cursor is not None:
            if cursor.element.value == value:
                return cursor.element
            cursor = cursor.next_node
        return None

    # Searcheses the list for a node whose element is the same element as the
    # argument. If found, the matching node is removed from the list and True is
    # returned. Otherwise the list isn't altered and False is returned.
    def delete(self, element):
        if self.head_node.element is element:
            self.head_node = self.head_node.next_node
            return True
        prev_node = self.head_node
        cursor = self.head_node.next_node
        while cursor is not None:
            if cursor.element is element:
                prev_node.next_node = cursor.next_node
                return True
            prev_node = cursor
            cursor = cursor.next_node
        return False

    # Creates a new element with the argument as a value, and makes a new node
    # with that element. If the list is empty that node becomes the only node in
    # the list, otherwise the new node is appended to the end of the list.
    def add(self, value):
        element = String_Element(value)
        new_node = Singly_Linked_List_Node(element)
        if self.head_node is None:
            self.head_node = new_node
        else:
            this_node = self.head_node
            while this_node.next_node is not None:
                this_node = this_node.next_node
            this_node.next_node = new_node

    # Creates a list and populates it with the value of every element of every
    # node in the list, in order, and returns it.
    def values(self):
        if self.head_node is None:
            return []
        this_node = self.head_node
        retval = list()
        while this_node is not None:
            retval.append(this_node.element.value)
            this_node = this_node.next_node
        return retval


# A node in a singly linked list.
class Singly_Linked_List_Node(List_Node_Impl):
    __slots__ = "next_node", "element"

    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


# Singly-linked-list implementation. Every node has reference to both the
# previous node and the next node.
class Doubly_Linked_List(Singly_Linked_List):
    __slots__ = "head_node", "tail_node"

    def __init__(self):
        self.head_node = self.tail_node = None

    # Creates a new element with the argument as a value, and makes a new node
    # with that element. If the list is empty that node becomes the only node in
    # the list, otherwise the new node is appended to the end of the list.
    def add(self, value):
        new_element = String_Element(value)
        new_node = Doubly_Linked_List_Node(new_element)
        if self.head_node is None:
            self.head_node = self.tail_node = new_node
        else:
            last_node = self.tail_node
            last_node.next_node = new_node
            new_node.prev_node = last_node
            self.tail_node = new_node

    # Searcheses the list for a node whose element is the same element as the
    # argument. If found, the matching node is removed from the list and True is
    # returned. Otherwise the list isn't altered and False is returned.
    def delete(self, element):
        if self.head_node is None:
            return False
        elif self.head_node.element is element:
            if self.head_node.next_node is None:
                self.head_node = self.tail_node = None
            else:
                new_first_node = self.head_node.next_node
                new_first_node.prev_node = None
                self.head_node = new_first_node
        elif self.tail_node.element is element:
            self.tail_node.prev_node.next_node = None
            self.tail_node = self.tail_node.prev_node
        else:
            cursor = self.head_node.next_node
            while cursor is not None:
                if cursor.element is element:
                    cursor.prev_node.next_node = cursor.next_node
                    cursor.next_node.prev_node = cursor.prev_node
                    return True
                cursor = cursor.next_node
            return False


# A node in a doubly linked list.
class Doubly_Linked_List_Node(List_Node_Impl):
    __slots__ = "prev_node", "next_node", "element"

    def __init__(self, element=None, prev_node=None, next_node=None):
        self.element = element
        self.prev_node = prev_node
        self.next_node = next_node


# Emulates a list using a dict where the indexes are keys and the elements are
# values. JavaScript-style list.
class Dict_Based_List(List_Impl):
    __slots__ = 'data_store',

    def __init__(self):
        self.data_store = dict()

    # Searches the list for an element whose value attribute equals the value
    # argument. Returns that element if found, otherwise returns None.
    def find(self, value):
        for element in self.data_store.values():
            if element.value == value:
                return element
        return None

    # Creates a new element with the argument as a value, and makes a new node
    # with that element. If the list is empty that node becomes the only node in
    # the list, otherwise the new node is appended to the end of the list.
    def add(self, value):
        new_element = String_Element(value)
        if not self.data_store:
            self.data_store[0] = new_element
        else:
            new_index = max(self.data_store.keys()) + 1
            self.data_store[new_index] = new_element

    # Searcheses the list for a node whose element is the same element as the
    # argument. If found, the matching node is removed from the list and True is
    # returned. Otherwise the list isn't altered and False is returned.
    def delete(self, element_to_delete):
        delete_key = None
        for key, element_in_list in self.data_store.items():
            if element_in_list is element_to_delete:
                delete_key = key
                break
        if delete_key is not None:
            del self.data_store[delete_key]
            return True
        else:
            return False

    # Creates a list and populates it with the value of every element of every
    # node in the list, in order, and returns it.
    def values(self):
        return [element.value for key, element in sorted(self.data_store.items())]


# Q&A
#
# "There’s nothing magical or surprising in list implementations, but there
# are a fair number of boundary conditions. For example, when deleting from the
# singly-linked list, did you have to deal with the case of deleting the first
# element in the list specially?"
#
# Yes. And in the doubly linked list, I had to handle both deleting the first
# element and deleting the last element specially.
#
#
# "For this kata, concentrate on ways of removing as many of these boundary
# conditions as possible. Then ask yourself: Is the resulting code, which will
# contain fewer special cases, easier to read and maintain? How easy was it to
# eliminate these special cases? Were there trade-offs, where removing a special
# case in one area complicated the code in another. Is there a sweet-spot when
# it comes to simplifying code?"
#
# Frankly I didn't do this. Implementing a linked list is dicey enough on its
# own. It made me think of this quote:
#
# "Debugging is twice as hard as writing the code in the first place. Therefore,
# if you write the code as cleverly as possible, you are, by definition, not
# smart enough to debug it."
# —Brian W. Kernighan
#
# Debugging the doubly linked list was like that. Eliminating boundary
# conditions would be clever programming of that sort. It's better to write more
# readable code.
