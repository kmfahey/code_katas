#!/usr/bin/python3


def compute(intstr):
    intval = int(intstr)
    towrite = []
    if intval % 3 == 0:
        towrite.append("Foo")
    if intval % 5 == 0:
        towrite.append("Bar")
    if intval % 7 == 0:
        towrite.append("Qix")
    for char in intstr:
        if char == "3":
            towrite.append("Foo")
        elif char == "5":
            towrite.append("Bar")
        elif char == "7":
            towrite.append("Qix")
    return str.join("", towrite) if towrite else intstr
