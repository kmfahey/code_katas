# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose

import copy


def test_update_quality_plus_5_dexterity_vest():
    argl = ('+5 Dexterity Vest', -1, 0)
    item_obj1 = Item(*argl)
    new_item_obj1 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj1])
    gilded_rose_obj.update_quality()
    assert new_item_obj1.sell_in == -2

    argl = ('+5 Dexterity Vest', -1, 25)
    item_obj2 = Item(*argl)
    new_item_obj2 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj2])
    gilded_rose_obj.update_quality()
    assert new_item_obj2.sell_in == -2
    assert new_item_obj2.quality == 23

    argl = ('+5 Dexterity Vest', -1, 50)
    item_obj3 = Item(*argl)
    new_item_obj3 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj3])
    gilded_rose_obj.update_quality()
    assert new_item_obj3.sell_in == -2
    assert new_item_obj3.quality == 48

    argl = ('+5 Dexterity Vest', 5, 0)
    item_obj4 = Item(*argl)
    new_item_obj4 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj4])
    gilded_rose_obj.update_quality()
    assert new_item_obj4.sell_in == 4

    argl = ('+5 Dexterity Vest', 5, 25)
    item_obj5 = Item(*argl)
    new_item_obj5 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj5])
    gilded_rose_obj.update_quality()
    assert new_item_obj5.sell_in == 4
    assert new_item_obj5.quality == 24

    argl = ('+5 Dexterity Vest', 5, 50)
    item_obj6 = Item(*argl)
    new_item_obj6 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj6])
    gilded_rose_obj.update_quality()
    assert new_item_obj6.sell_in == 4
    assert new_item_obj6.quality == 49

    argl = ('+5 Dexterity Vest', 10, 0)
    item_obj7 = Item(*argl)
    new_item_obj7 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj7])
    gilded_rose_obj.update_quality()
    assert new_item_obj7.sell_in == 9

    argl = ('+5 Dexterity Vest', 10, 25)
    item_obj8 = Item(*argl)
    new_item_obj8 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj8])
    gilded_rose_obj.update_quality()
    assert new_item_obj8.sell_in == 9
    assert new_item_obj8.quality == 24

    argl = ('+5 Dexterity Vest', 10, 50)
    item_obj9 = Item(*argl)
    new_item_obj9 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj9])
    gilded_rose_obj.update_quality()
    assert new_item_obj9.sell_in == 9
    assert new_item_obj9.quality == 49

    argl = ('+5 Dexterity Vest', 15, 0)
    item_obj10 = Item(*argl)
    new_item_obj10 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj10])
    gilded_rose_obj.update_quality()
    assert new_item_obj10.sell_in == 14

    argl = ('+5 Dexterity Vest', 15, 25)
    item_obj11 = Item(*argl)
    new_item_obj11 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj11])
    gilded_rose_obj.update_quality()
    assert new_item_obj11.sell_in == 14
    assert new_item_obj11.quality == 24

    argl = ('+5 Dexterity Vest', 15, 50)
    item_obj12 = Item(*argl)
    new_item_obj12 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj12])
    gilded_rose_obj.update_quality()
    assert new_item_obj12.sell_in == 14
    assert new_item_obj12.quality == 49


def test_update_quality_aged_brie():
    argl = ('Aged Brie', -1, 0)
    item_obj1 = Item(*argl)
    new_item_obj1 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj1])
    gilded_rose_obj.update_quality()
    assert new_item_obj1.sell_in == -2
    assert new_item_obj1.quality == 2

    argl = ('Aged Brie', -1, 25)
    item_obj2 = Item(*argl)
    new_item_obj2 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj2])
    gilded_rose_obj.update_quality()
    assert new_item_obj2.sell_in == -2
    assert new_item_obj2.quality == 27

    argl = ('Aged Brie', -1, 50)
    item_obj3 = Item(*argl)
    new_item_obj3 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj3])
    gilded_rose_obj.update_quality()
    assert new_item_obj3.sell_in == -2

    argl = ('Aged Brie', 5, 0)
    item_obj4 = Item(*argl)
    new_item_obj4 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj4])
    gilded_rose_obj.update_quality()
    assert new_item_obj4.sell_in == 4
    assert new_item_obj4.quality == 1

    argl = ('Aged Brie', 5, 25)
    item_obj5 = Item(*argl)
    new_item_obj5 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj5])
    gilded_rose_obj.update_quality()
    assert new_item_obj5.sell_in == 4
    assert new_item_obj5.quality == 26

    argl = ('Aged Brie', 5, 50)
    item_obj6 = Item(*argl)
    new_item_obj6 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj6])
    gilded_rose_obj.update_quality()
    assert new_item_obj6.sell_in == 4

    argl = ('Aged Brie', 10, 0)
    item_obj7 = Item(*argl)
    new_item_obj7 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj7])
    gilded_rose_obj.update_quality()
    assert new_item_obj7.sell_in == 9
    assert new_item_obj7.quality == 1

    argl = ('Aged Brie', 10, 25)
    item_obj8 = Item(*argl)
    new_item_obj8 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj8])
    gilded_rose_obj.update_quality()
    assert new_item_obj8.sell_in == 9
    assert new_item_obj8.quality == 26

    argl = ('Aged Brie', 10, 50)
    item_obj9 = Item(*argl)
    new_item_obj9 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj9])
    gilded_rose_obj.update_quality()
    assert new_item_obj9.sell_in == 9

    argl = ('Aged Brie', 15, 0)
    item_obj10 = Item(*argl)
    new_item_obj10 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj10])
    gilded_rose_obj.update_quality()
    assert new_item_obj10.sell_in == 14
    assert new_item_obj10.quality == 1

    argl = ('Aged Brie', 15, 25)
    item_obj11 = Item(*argl)
    new_item_obj11 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj11])
    gilded_rose_obj.update_quality()
    assert new_item_obj11.sell_in == 14
    assert new_item_obj11.quality == 26

    argl = ('Aged Brie', 15, 50)
    item_obj12 = Item(*argl)
    new_item_obj12 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj12])
    gilded_rose_obj.update_quality()
    assert new_item_obj12.sell_in == 14


def test_update_quality_backstage_passes_to_a_tafkal80etc_concert():
    argl = ('Backstage passes to a TAFKAL80ETC concert', -1, 0)
    item_obj1 = Item(*argl)
    new_item_obj1 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj1])
    gilded_rose_obj.update_quality()
    assert new_item_obj1.sell_in == -2

    argl = ('Backstage passes to a TAFKAL80ETC concert', -1, 25)
    item_obj2 = Item(*argl)
    new_item_obj2 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj2])
    gilded_rose_obj.update_quality()
    assert new_item_obj2.sell_in == -2
    assert new_item_obj2.quality == 0

    argl = ('Backstage passes to a TAFKAL80ETC concert', -1, 50)
    item_obj3 = Item(*argl)
    new_item_obj3 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj3])
    gilded_rose_obj.update_quality()
    assert new_item_obj3.sell_in == -2
    assert new_item_obj3.quality == 0

    argl = ('Backstage passes to a TAFKAL80ETC concert', 5, 0)
    item_obj4 = Item(*argl)
    new_item_obj4 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj4])
    gilded_rose_obj.update_quality()
    assert new_item_obj4.sell_in == 4
    assert new_item_obj4.quality == 3

    argl = ('Backstage passes to a TAFKAL80ETC concert', 5, 25)
    item_obj5 = Item(*argl)
    new_item_obj5 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj5])
    gilded_rose_obj.update_quality()
    assert new_item_obj5.sell_in == 4
    assert new_item_obj5.quality == 28

    argl = ('Backstage passes to a TAFKAL80ETC concert', 5, 50)
    item_obj6 = Item(*argl)
    new_item_obj6 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj6])
    gilded_rose_obj.update_quality()
    assert new_item_obj6.sell_in == 4

    argl = ('Backstage passes to a TAFKAL80ETC concert', 10, 0)
    item_obj7 = Item(*argl)
    new_item_obj7 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj7])
    gilded_rose_obj.update_quality()
    assert new_item_obj7.sell_in == 9
    assert new_item_obj7.quality == 2

    argl = ('Backstage passes to a TAFKAL80ETC concert', 10, 25)
    item_obj8 = Item(*argl)
    new_item_obj8 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj8])
    gilded_rose_obj.update_quality()
    assert new_item_obj8.sell_in == 9
    assert new_item_obj8.quality == 27

    argl = ('Backstage passes to a TAFKAL80ETC concert', 10, 50)
    item_obj9 = Item(*argl)
    new_item_obj9 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj9])
    gilded_rose_obj.update_quality()
    assert new_item_obj9.sell_in == 9

    argl = ('Backstage passes to a TAFKAL80ETC concert', 15, 0)
    item_obj10 = Item(*argl)
    new_item_obj10 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj10])
    gilded_rose_obj.update_quality()
    assert new_item_obj10.sell_in == 14
    assert new_item_obj10.quality == 1

    argl = ('Backstage passes to a TAFKAL80ETC concert', 15, 25)
    item_obj11 = Item(*argl)
    new_item_obj11 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj11])
    gilded_rose_obj.update_quality()
    assert new_item_obj11.sell_in == 14
    assert new_item_obj11.quality == 26

    argl = ('Backstage passes to a TAFKAL80ETC concert', 15, 50)
    item_obj12 = Item(*argl)
    new_item_obj12 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj12])
    gilded_rose_obj.update_quality()
    assert new_item_obj12.sell_in == 14


def test_update_quality_conjured_mana_cake():
    argl = ('Conjured Mana Cake', -1, 0)
    item_obj1 = Item(*argl)
    new_item_obj1 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj1])
    gilded_rose_obj.update_quality()
    assert new_item_obj1.sell_in == -2

    argl = ('Conjured Mana Cake', -1, 25)
    item_obj2 = Item(*argl)
    new_item_obj2 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj2])
    gilded_rose_obj.update_quality()
    assert new_item_obj2.sell_in == -2
    assert new_item_obj2.quality == 23

    argl = ('Conjured Mana Cake', -1, 50)
    item_obj3 = Item(*argl)
    new_item_obj3 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj3])
    gilded_rose_obj.update_quality()
    assert new_item_obj3.sell_in == -2
    assert new_item_obj3.quality == 48

    argl = ('Conjured Mana Cake', 5, 0)
    item_obj4 = Item(*argl)
    new_item_obj4 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj4])
    gilded_rose_obj.update_quality()
    assert new_item_obj4.sell_in == 4

    argl = ('Conjured Mana Cake', 5, 25)
    item_obj5 = Item(*argl)
    new_item_obj5 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj5])
    gilded_rose_obj.update_quality()
    assert new_item_obj5.sell_in == 4
    assert new_item_obj5.quality == 24

    argl = ('Conjured Mana Cake', 5, 50)
    item_obj6 = Item(*argl)
    new_item_obj6 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj6])
    gilded_rose_obj.update_quality()
    assert new_item_obj6.sell_in == 4
    assert new_item_obj6.quality == 49

    argl = ('Conjured Mana Cake', 10, 0)
    item_obj7 = Item(*argl)
    new_item_obj7 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj7])
    gilded_rose_obj.update_quality()
    assert new_item_obj7.sell_in == 9

    argl = ('Conjured Mana Cake', 10, 25)
    item_obj8 = Item(*argl)
    new_item_obj8 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj8])
    gilded_rose_obj.update_quality()
    assert new_item_obj8.sell_in == 9
    assert new_item_obj8.quality == 24

    argl = ('Conjured Mana Cake', 10, 50)
    item_obj9 = Item(*argl)
    new_item_obj9 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj9])
    gilded_rose_obj.update_quality()
    assert new_item_obj9.sell_in == 9
    assert new_item_obj9.quality == 49

    argl = ('Conjured Mana Cake', 15, 0)
    item_obj10 = Item(*argl)
    new_item_obj10 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj10])
    gilded_rose_obj.update_quality()
    assert new_item_obj10.sell_in == 14

    argl = ('Conjured Mana Cake', 15, 25)
    item_obj11 = Item(*argl)
    new_item_obj11 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj11])
    gilded_rose_obj.update_quality()
    assert new_item_obj11.sell_in == 14
    assert new_item_obj11.quality == 24

    argl = ('Conjured Mana Cake', 15, 50)
    item_obj12 = Item(*argl)
    new_item_obj12 = Item(*argl)
    gilded_rose_obj = GildedRose([new_item_obj12])
    gilded_rose_obj.update_quality()
    assert new_item_obj12.sell_in == 14
    assert new_item_obj12.quality == 49

