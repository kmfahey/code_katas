# -*- coding: utf-8 -*-

from gilded_rose import Item, GildedRose


def test_foo():
    items = [Item("foo", 0, 0)]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert "foo" == items[0].name

def test_update_quality_1():
    item_obj = Item("Foo", 10, 30)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 9
    assert item_obj.quality == 29

def test_update_quality_2():
    item_obj = Item("Foo", 10, 0)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 9
    assert item_obj.quality == 0

def test_update_quality_3():
    item_obj = Item("Sulfuras, Hand of Ragnaros", 10, 45)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 10
    assert item_obj.quality == 45

def test_update_quality_4():
    item_obj = Item("Sulfuras, Hand of Ragnaros", 10, 50)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 10
    assert item_obj.quality == 50

def test_update_quality_5():
    item_obj = Item("Aged Brie", 10, 30)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 9
    assert item_obj.quality == 31

def test_update_quality_6():
    item_obj = Item("Aged Brie", 10, 50)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 9
    assert item_obj.quality == 50

def test_update_quality_7():
    item_obj = Item("Backstage passes to a TAFKAL80ETC concert", 15, 50)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 14
    assert item_obj.quality == 50

def test_update_quality_8():
    item_obj = Item("Backstage passes to a TAFKAL80ETC concert", 15, 30)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 14
    assert item_obj.quality == 31

def test_update_quality_9():
    item_obj = Item("Backstage passes to a TAFKAL80ETC concert", 10, 30)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 9
    assert item_obj.quality == 32

def test_update_quality_10():
    item_obj = Item("Backstage passes to a TAFKAL80ETC concert", 5, 30)
    gilded_rose_obj = GildedRose([item_obj])
    gilded_rose_obj.update_quality()
    assert item_obj.sell_in == 4
    assert item_obj.quality == 33
