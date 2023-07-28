# -*- coding: utf-8 -*-

import operator

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie":
                    # “Aged Brie” actually increases in Quality the older it gets
                    # The Quality of an item is never more than 50
                    if item.quality < 50:
                        item.quality += 1
                    item.sell_in -= 1
                    if item.sell_in < 0 and item.quality < 50:
                        item.quality += 1
                case "Backstage passes to a TAFKAL80ETC concert":
                    # “Backstage passes”, like aged brie, increases in Quality as it’s SellIn value approaches
                    # The Quality of an item is never more than 50
                    if item.quality < 50:
                        # Quality increases by 3 when there are 5 days or less
                        if item.sell_in < 6:
                            item.quality += 3
                        # Quality increases by 2 when there are 10 days or less
                        elif item.sell_in < 11:
                            item.quality += 2
                        # but Quality drops to 0 after the concert
                        else:
                            item.quality += 1
                    item.sell_in -= 1
                    if item.sell_in < 0:
                        item.quality = 0
                case "Sulfuras, Hand of Ragnaros":
                    # “Sulfuras”, being a legendary item, never has to be sold or decreases in Quality
                    pass
                case name if name.startswith("Conjured"):
                    item.sell_in -= 1
                    # if the sell-by date has passed, quality degrades twice as fast.
                    # The Quality of an item is never negative
                    # “Conjured” items degrade in Quality twice as fast as normal items
                    if item.sell_in < 0 and item.quality > 1:
                        item.quality -= 4
                    elif item.quality > 0:
                        item.quality -= 2
                case _:
                    item.sell_in -= 1
                    # if the sell-by date has passed, quality degrades twice as fast.
                    # The Quality of an item is never negative
                    if item.sell_in < 0 and item.quality > 1:
                        item.quality -= 2
                    elif item.quality > 0:
                        item.quality -= 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
