class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_quality()
    #         if item.name == "Sulfuras, Hand of Ragnaros":
    #             continue
    #
    #         item.sell_in = item.sell_in - 1
    #
    #         if item.name == "Backstage passes to a TAFKAL80ETC concert" and self._sell_in_is_negative(item):
    #             item.quality = item.quality - item.quality
    #
    #         if item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"] and self._sell_in_is_negative(item):
    #             self._decrease_quality_by_one_if_quality_greather_than_zero(item)
    #
    #         if item.name not in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
    #             self._decrease_quality_by_one_if_quality_greather_than_zero(item)
    #
    #         if item.name in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"] and self._sell_in_is_negative(item):
    #             self._increment_quality_by_one_if_quality_under_fifty(item)
    #
    #         if item.name in ["Aged Brie", "Backstage passes to a TAFKAL80ETC concert"]:
    #             self._increment_quality_by_one_if_quality_under_fifty(item)
    #
    #         if item.name == "Backstage passes to a TAFKAL80ETC concert":
    #             self._handle_backstage_quality_increment(item)
    #
    #
    # def _handle_backstage_quality_increment(self, item):
    #     if item.sell_in < 11:
    #         self._increment_quality_by_one_if_quality_under_fifty(item)
    #     if item.sell_in < 6:
    #         self._increment_quality_by_one_if_quality_under_fifty(item)
    #
    # def _increment_quality_by_one_if_quality_under_fifty(self, item):
    #     if item.quality < 50:
    #         item.quality = item.quality + 1
    #
    # def _decrease_quality_by_one_if_quality_greather_than_zero(self, item):
    #     if item.quality > 0:
    #         item.quality = item.quality - 1
    #
    # def _sell_in_is_negative(self, item):
    #     return item.sell_in < 0
