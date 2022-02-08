import unittest

from src.gilded_rose import Item, GildedRose

A_NAME = 'a_name'


class GildedRoseTest(unittest.TestCase):
    def test_at_the_end_of_each_day_items_lowers_quality_and_sellin_by_one(self):
        items = [Item(A_NAME, 2, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expected_item = Item(A_NAME, 1, 1)
        self.assertEqual(expected_item.__dict__, items[0].__dict__)

    def test_once_the_sell_by_date_has_passed_quality_degrades_twice_as_fast(self):
        items = [Item(A_NAME, 0, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(2, items[0].quality)

    def test_the_quality_of_an_item_is_never_negative(self):
        items = [Item(A_NAME, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)

    def test_aged_brie_actually_increases_in_quality_the_older_it_gets_instead_of_decreasing(self):
        items = [Item("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(1, items[0].quality)

    def test_the_quality_of_an_item_is_never_more_than_fifty(self):
        items = [Item("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_has_to_be_sold_nor_decreases_in_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expected_item = Item("Sulfuras, Hand of Ragnaros", 2, 50)
        self.assertEqual(expected_item.__dict__, items[0].__dict__)

    def test_backstage_sell_in_decrease_can_be_negative(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_increases_quality_by_three_if_quality_lower_than_fifty(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 2, 44)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(47, items[0].quality)

    def test_sell_in_negative_increases_quality_twice_if_name_aged_brie_and_quality_under_fifty(self):
        items = [Item("Aged Brie", -1, 44)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(46, items[0].quality)


if __name__ == '__main__':
    unittest.main()
