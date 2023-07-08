#!/usr/bin/python3

import abc
import re


class Decorable(metaclass=abc.ABCMeta):
    @classmethod
    def _all_emoji(self):
        emoji_list = []
        for subclass in self.__subclasses__():
            if hasattr(subclass, "_emoji"):
                emoji_list.append(subclass._emoji)
        return emoji_list

    _emoji = abc.abstractproperty(lambda s: None)

    _cost = abc.abstractproperty(lambda s: None)

    name = abc.abstractproperty(lambda s: None)

    price = abc.abstractproperty(lambda s: None)

    __init__ = abc.abstractmethod(lambda s: None)

    __repr__ = abc.abstractmethod(lambda s: None)


### Pastry ABC & Pastry subclasses

class Pastry(Decorable):
    @classmethod
    def _all_pastry_emoji(self):
        return self._all_emoji()

    @property
    def name(self):
        return self._emoji

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

    @classmethod
    def _all_topping_emoji(self):
        return self._all_emoji()

    def __init__(self, contents):
        if not isinstance(contents, (Pastry, Topping)):
            raise ValueError("contents arg must be instance of either Pastry or Topping")
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

        all_topping_emoji = ''.join(Topping._all_topping_emoji())
        all_pastry_emoji = ''.join(Pastry._all_pastry_emoji())

        name_w_one_topping_re = re.compile(f"([{all_pastry_emoji}]) with ([{all_topping_emoji}])$")
        name_w_two_toppings_re = re.compile(f"([{all_pastry_emoji}]) with ([{all_topping_emoji}] and [{all_topping_emoji}])$")
        name_w_many_toppings_re = re.compile(f"([{all_pastry_emoji}]) with ((?:[{all_topping_emoji}], )+and [{all_topping_emoji}])$")

        inner_str = self.contents.name
        matched_one = name_w_one_topping_re.search(inner_str)
        if matched_one:
            cupcake = matched_one.group(1)
            emoji = [self._emoji, matched_one.group(2)]
            return f"{cupcake} with {emoji[0]} and {emoji[1]}"

        matched_two = name_w_two_toppings_re.search(inner_str)
        if matched_two:
            cupcake = matched_two.group(1)
            emoji = [self._emoji] + matched_two.group(2).split(" and ")
            return f"{cupcake} with {emoji[0]}, {emoji[1]}, and {emoji[2]}"

        matched_many = name_w_many_toppings_re.search(inner_str)
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
    _cost = 0.20
    _emoji = "🥜"


class Bundle:
    __slots__ = "contents",

    def __init__(self, contents=()):
        if not isinstance(contents, abc.Sequence):
            raise ValueError("contents arg must be a sequence")
        contents = tuple(contents)
        if not len(contents):
            raise ValueError("contents arg must not be zero-length")
        for index, elem in enumerate(contents):
            if not isinstance(elem, (Bundle, Pastry, Topping)):
                raise ValueError(f"error on elem at index {index} in contents arg: must be an instance of "
                                 f"Bundle, Pastry or Topping (was {elem.__class__.__name__})")
        self.contents = contents

    @property
    def price(self):
        return sum(elem.price if isinstance(elem, Bundle) else elem.price * 0.90 for elem in self.contents)

    @property
    def description(self):
        contents_nested_list = self._contents_to_nested_list()

        contents_markdown = self._contents_to_nested_list(contents_nested_list)

        return "a bundle that contains:\n" + contents_markdown

    # This method generated by ChatGPT with GPT-4
    def _contents_to_nested_list(self):
        result = []  # This will store our nested list
        stack = [(self.contents, result)]  # Start with initial contents

        while stack:
            current_contents, current_result = stack.pop()

            for item in current_contents:
                if isinstance(item, Bundle):
                    new_list = []
                    current_result.append(new_list)
                    stack.append((item.contents, new_list))  # Add Bundle's contents to the stack for further processing
                else:
                    current_result.append(item)

        return result

    # This method generated by ChatGPT with GPT-4
    def _nested_list_to_markdown(self, nested_list, indent=0):
        markdown = ""

        # Add a "bundle" line at every level, but only format as a list item if not at the outermost level
        markdown += '    ' * indent + ('- ' if indent > 0 else '') + 'a bundle that contains:\n'

        for item in nested_list:
            # If the item is a list, we recursively process it with an increased indentation
            if isinstance(item, list):
                markdown += self._nested_list_to_markdown(item, indent + 1)
            else:
                # Assume that each of Elem instances has a `name` attribute
                # Increase indentation level by 1 for the list elements
                markdown += '    ' * (indent + 1) + '- ' + item.name + '\n'

        return markdown
