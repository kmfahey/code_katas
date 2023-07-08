#!/usr/bin/python3

import abc
import re


class Decorable(metaclass=abc.ABCMeta):
    _emoji = abc.abstractproperty(lambda s: None)

    _cost = abc.abstractproperty(lambda s: None)

    name = abc.abstractproperty(lambda s: None)

    price = abc.abstractproperty(lambda s: None)

    __init__ = abc.abstractmethod(lambda s: None)

    __repr__ = abc.abstractmethod(lambda s: None)


### Pastry ABC & Pastry subclasses

class Pastry(Decorable):
    @property
    def name(self):
        return f"a {self._emoji}"

    @property
    def price(self):
        return self._cost

    def __repr__(self):
        return f"{self.__class__.__name__}()"


class Cookie(Pastry):
    _cost = 2.00
    _emoji = "🍪"

    def __init__(self):
        pass


class Cupcake(Pastry):
    _cost = 1.00
    _emoji = "🧁"

    def __init__(self):
        pass


class Pie(Pastry):
    _cost = 9.00
    _emoji = "🥧"

    def __init__(self):
        pass


class Cake(Pastry):
    _cost = 9.00
    _emoji = "🎂"

    def __init__(self):
        pass


class Shortcake(Pastry):
    _cost = 4.00
    _emoji = "🍰"

    def __init__(self):
        pass


### Topping ABC & Topping subclasses

class Topping(Decorable):
    __slots__ = "contents",

    def __init__(self, contents):
        self.contents = contents

    @property
    def price(self):
        return round(self._cost + self.contents.price, 2)

    @property
    def name(self):
        if isinstance(self.contents, Pastry):
            return self.contents.name + f" with {self._emoji}"

        # This block calls str() on contents. The regexes parse the current
        # stack of emoji out of the result, then builds a new grammatically
        # correct comma-separated list with this object's emoji attached and
        # returns them. This happens on each step of the recursive str() call so
        # the retval is always grammatically correct in case this name() call
        # is the outermost in the decorator stack.

        inner_str = self.contents.name
        matched_one = re.search("(🧁) with ([🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_one:
            cupcake = matched_one.group(1)
            emoji = [self._emoji, matched_one.group(2)]
            return f"{cupcake} with {emoji[0]} and {emoji[1]}"

        matched_two = re.search("(🧁) with ([🍮 🍯 🍬 🍪 🍫] and [🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_two:
            cupcake = matched_two.group(1)
            emoji = [self._emoji] + matched_two.group(2).split(" and ")
            return f"{cupcake} with {emoji[0]}, {emoji[1]}, and {emoji[2]}"

        matched_many = re.search("(🧁) with ((?:[🍮 🍯 🍬 🍪 🍫], )+and [🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_many:
            cupcake = matched_many.group(1)
            emoji = [self._emoji] + re.split(", and |, |and", matched_many.group(2))
            toppings = ", ".join(emoji[:-1] + ["and " + emoji[-1]])
            return f"{cupcake} with {toppings}"

        raise RuntimeError("Can't happen error: none of the regexes matched the text from inner str() call.")

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.contents)})"


class Honey(Topping):
    _cost = 0.50
    _emoji = "🍯"


class Whipped_Custard(Topping):
    _cost = 0.60
    _emoji = "🍮"


class Crushed_Candy(Topping):
    _cost = 0.50
    _emoji = "🍬"


class Chocolate(Topping):
    _cost = 0.10
    _emoji = "🍫"


class Crumbled_Cookies(Topping):
    _cost = 0.20
    _emoji = "🍪"


class Nuts(Topping):
    _cost = 0.10
    _emoji = "🥜"
