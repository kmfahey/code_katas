#!/usr/bin/python3

import collections


__all__ = ["Rule", "Checkout"]


# Checkout rule. Lists a number that is the quantity of the item the rule can be
# applied to, and the price that quantity costs.
Rule = collections.namedtuple("Rule", ["number", "price"])


# Implements a Checkout machine class per the spec.
class Checkout:
    __slots__ = "pricing_rules", "item_qtys"

    def __init__(self, pricing_rules):
        self.pricing_rules = pricing_rules
        self.item_qtys = dict(A=0, B=0, C=0, D=0)

    # Add one instance of the scanned item to the quantities.
    def scan(self, item):
        self.item_qtys[item] += 1

    # Calculates the total cost of all the items in the item_qtys store,
    # applying the stored rules.
    def total(self):
        running_total = 0
        for item, rules in self.pricing_rules.items():

            # If there's 2 rules, then there's a unit rule followed by a rule
            # for batches. First the batch rule is applied as many times as it
            # can be while decementing the quantity each time. Then the unit
            # rule is applied to the remaining quantity, if any.
            if len(rules) == 2:
                unit_rule, batch_rule = rules
                item_qty = self.item_qtys[item]
                batches = item_qty // batch_rule.number
                units = item_qty % batch_rule.number
                running_total += batches * batch_rule.price + units * unit_rule.price

            # If there's only 1 rule, then it's a batch rule. It's applied to
            # the remaining quantity.
            else:
                unit_rule, = rules
                item_qty = self.item_qtys[item]
                running_total += item_qty * unit_rule.price

        return running_total

# Q&A
#
# "To some extent, this is just a fun little problem. But underneath the covers,
# it’s a stealth exercise in decoupling. The challenge description doesn’t
# mention the format of the pricing rules."
#
# "How can these be specified in such a way that the checkout doesn’t know
# about particular items and their pricing strategies?"
#
# If you specify a Rule abstract base class that leaves undefined a
# compute_price method, and then for each different style of rule setup a
# subclass of Rule that has a compute_price method that computes the price
# according to its particular logic, and then the total() method just calls
# compute_price while only handling the rules as instances of the Rule class,
# then that's how.
#
#
# "How can we make the design flexible enough so that we can add new styles of
# pricing rule in the future?"
#
# See above, actually.
