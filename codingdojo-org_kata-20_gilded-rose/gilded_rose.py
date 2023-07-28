# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            match item.name:
                case "Aged Brie" if item.quality < 50:
                    item.quality += 1
                case "Backstage passes to a TAFKAL80ETC concert" if item.quality < 50:
                    if item.sell_in < 6:
                        item.quality += 3
                    elif item.sell_in < 11:
                        item.quality += 2
                    else:
                        item.quality += 1
                case "Sulfuras, Hand of Ragnaros":
                    pass
                case _ if item.quality > 0:
                    item.quality -= 1

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1

            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        item.quality = 0
                    elif item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
                        item.quality -= 1
                elif item.quality < 50:
                    item.quality += 1


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
