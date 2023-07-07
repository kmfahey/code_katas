#!/usr/bin/python3

import abc
# import re


class Decorable(metaclass=abc.ABCMeta):
    __slots__ = "price", "emoji"

#    @property
#    def all_cupc_tpg_emoji(self):
#        return [subclass.emoji for subclass in type(self).__subclasses__() if not isinstance(subclass, abc.ABCMeta)]

    @abc.abstractproperty
    def emoji(self):
        pass

    @abc.abstractproperty
    def price(self):
        pass

    @abc.abstractmethod
    def __init__(self):
        pass


class Cupcake(Decorable):
    price = 1.99
    emoji = "🧁"

    def __init__(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}()"

    def __str__(self):
        return f"a {self.emoji}"


class Topping(Decorable):
    __slots__ = "beneath_this",

    def __init__(self, beneath_this):
        self.beneath_this = beneath_this

    def __str__(self):
        if isinstance(self.beneath_this, Cupcake):
            return str(self.beneath_this) + f" with {self.emoji}"
        else:
            # TODO: revamp this so at each recursive step it strips off any
            # comma-separated list formatting created by the inner str() call
            # and then applies a new comma-separated list formatting correct to
            # the added topping.
            return str(self.beneath_this) + f" and {self.emoji}"

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
    emoji = "🍫 "


class Crumbled_Cookies(Topping):
    price = 0.19
    emoji = "🍪 "
