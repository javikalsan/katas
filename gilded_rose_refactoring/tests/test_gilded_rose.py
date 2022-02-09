import unittest

from src.item_factory import ItemFactory
from src.gilded_rose import GildedRose

A_NAME = 'a_name'
item_factory = ItemFactory()


class GildedRoseTest(unittest.TestCase):
    def test_at_the_end_of_each_day_items_lowers_quality_and_sellin_by_one(self):
        items = [item_factory.create(A_NAME, 2, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expected_item = item_factory.create(A_NAME, 1, 1)
        self.assertEqual(expected_item.__dict__, items[0].__dict__)

    def test_once_the_sell_by_date_has_passed_quality_degrades_twice_as_fast(self):
        items = [item_factory.create(A_NAME, 0, 4)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(2, items[0].quality)

    def test_the_quality_of_an_item_is_never_negative(self):
        items = [item_factory.create(A_NAME, 0, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(0, items[0].quality)

    def test_aged_brie_actually_increases_in_quality_the_older_it_gets_instead_of_decreasing(self):
        items = [item_factory.create("Aged Brie", 2, 0)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(1, items[0].quality)

    def test_the_quality_of_an_item_is_never_more_than_fifty(self):
        items = [item_factory.create("Aged Brie", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_sulfuras_never_has_to_be_sold_nor_decreases_in_quality(self):
        items = [item_factory.create("Sulfuras, Hand of Ragnaros", 2, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        expected_item = item_factory.create("Sulfuras, Hand of Ragnaros", 2, 50)
        self.assertEqual(expected_item.__dict__, items[0].__dict__)

    def test_backstage_sell_in_decrease_can_be_negative(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 0, 49)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(-1, items[0].sell_in)

    def test_backstage_increases_quality_by_three_if_quality_lower_than_fifty(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 2, 44)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(47, items[0].quality)

    def test_backstage_increases_quality_by_two_if_seeling_between_ten_and_six(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 7, 44)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(46, items[0].quality)

    def test_backstage_increases_quality_by_one_if_seeling_greather_than_10(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 11, 44)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(45, items[0].quality)

    def test_backstage_dont_rebase_quality_50_limit_value(self):
        items = [item_factory.create("Backstage passes to a TAFKAL80ETC concert", 11, 50)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(50, items[0].quality)

    def test_conjured_decrease_quality_by_two_if_quality_greather_than_two(self):
        items = [item_factory.create("Conjured Mana Cake", 11, 2)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(2, items[0].quality)

    def test_conjured_not_drecrease_quality_if_quality_lower_than_2(self):
        items = [item_factory.create("Conjured Mana Cake", 11, 3)]
        gilded_rose = GildedRose(items)

        gilded_rose.update_quality()

        self.assertEqual(1, items[0].quality)

    def test_regular_item_representation_contract(self):
        items = [item_factory.create(A_NAME, 11, 3)]

        self.assertEqual("a_name, 11, 3", items[0].__repr__())


if __name__ == '__main__':
    unittest.main()
