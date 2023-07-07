#!/usr/bin/python3

import abc
import re


class Decorable(metaclass=abc.ABCMeta):
    @abc.abstractproperty
    def emoji(self):
        pass

    @abc.abstractproperty
    def price(self):
        pass

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def __repr__(self):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass


class Pastry(Decorable):
    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"a {self.emoji}"


class Cookie(Pastry):
    price = 2.99
    emoji = "🍪"

    def __init__(self):
        pass


class Cupcake(Pastry):
    price = 1.99
    emoji = "🧁"

    def __init__(self):
        pass


class Pie(Pastry):
    price = 8.99
    emoji = "🥧"

    def __init__(self):
        pass


class Cake(Pastry):
    price = 8.99
    emoji = "🎂"

    def __init__(self):
        pass


class Shortcake(Pastry):
    price = 3.99
    emoji = "🍰"

    def __init__(self):
        pass


class Topping(Decorable):
    __slots__ = "beneath_this",

    def __init__(self, beneath_this):
        self.beneath_this = beneath_this

    def __str__(self):
        if isinstance(self.beneath_this, Cupcake):
            return str(self.beneath_this) + f" with {self.emoji}"

        # This block calls str() on beneath_this. The regexes parse the current
        # stack of emoji out of the result, then builds a new grammatically
        # correct comma-separated list with this object's emoji attached and
        # returns them. This happens on each step of the recursive str() call so
        # the retval is always grammatically correct in case this __str__ call
        # is the outermost in the decorator stack.

        inner_str = str(self.beneath_this)
        matched_one = re.search("(🧁) with ([🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_one:
            cupcake = matched_one.group(1)
            emoji = [self.emoji, matched_one.group(2)]
            return f"{cupcake} with {emoji[0]} and {emoji[1]}"

        matched_two = re.search("(🧁) with ([🍮 🍯 🍬 🍪 🍫] and [🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_two:
            cupcake = matched_two.group(1)
            emoji = [self.emoji] + matched_two.group(2).split(" and ")
            return f"{cupcake} with {emoji[0]}, {emoji[1]}, and {emoji[2]}"

        matched_many = re.search("(🧁) with ((?:[🍮 🍯 🍬 🍪 🍫], )+and [🍮 🍯 🍬 🍪 🍫])$", inner_str)
        if matched_many:
            cupcake = matched_many.group(1)
            emoji = [self.emoji] + re.split(", and |, |and", matched_many.group(2))
            toppings = ", ".join(emoji[:-1] + ["and " + emoji[-1]])
            return f"{cupcake} with {toppings}"

        raise RuntimeError("Can't happen error: none of the regexes matched the text from inner str() call.")

    def __repr__(self):
        return f"{self.__class__.__name__}({repr(self.beneath_this)})"

    def total_price(self):
        return round(self.price + self.beneath_this.total_price, 2)


class Honey(Topping):
    price = 0.49
    emoji = "🍯"


class Whipped_Custard(Topping):
    price = 0.59
    emoji = "🍮"


class Crushed_Candy(Topping):
    price = 0.49
    emoji = "🍬"


class Chocolate(Topping):
    price = 0.79
    emoji = "🍫"


class Crumbled_Cookies(Topping):
    price = 0.19
    emoji = "🍪"


class Nuts(Topping):
    price = 0.19
    emoji = "🥜"
