class ItemFactory(object):
    def create(self, name, sell_in, quality):
        if name == "Aged Brie": return AgedBrie(name, sell_in, quality)
        if name == "Sulfuras, Hand of Ragnaros": return Sulfuras(name, sell_in, quality)
        if name == "Backstage passes to a TAFKAL80ETC concert": return Backstage(name, sell_in, quality)
        if name == "Conjured Mana Cake": return Conjured(name, sell_in, quality)
        return RegularItem(name, sell_in, quality)


class RegularItem:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.quality = quality
        self.sell_in = sell_in

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update_quality(self):
        if 50 > self.quality > 0:
            self.quality = self.quality - self._compute_quality_drecrement()
        self.sell_in = self.sell_in - 1

    def _compute_quality_drecrement(self):
        if self.sell_in <= 0:
            return 2
        return 1


class AgedBrie(RegularItem):
    def update_quality(self):
        if self.quality < 50:
            self.quality = self.quality + 1
        self.sell_in = self.sell_in - 1


class Sulfuras(RegularItem):
    def update_quality(self):
        pass


class Conjured(RegularItem):
    def update_quality(self):
        self.quality = self.quality - self._compute_quality_decrement()
        self.sell_in = self.sell_in - 1

    def _compute_quality_decrement(self):
        if self.quality > 2:
            return 2
        return 0


class Backstage(RegularItem):
    def update_quality(self):
        self._handle_sellin_value_to_increment()
        self.quality = self._compute_quality_value()
        self.sell_in = self.sell_in - 1

    def _compute_quality_value(self):
        if self.quality > 50:
            return 50
        return self.quality

    def _handle_sellin_value_to_increment(self):
        if 10 >= self.sell_in > 5:
            self.quality = self.quality + 2
            return
        if 5 >= self.sell_in > 0:
            self.quality = self.quality + 3
            return
        if self.sell_in <= 0:
            self.quality = 0
        self.quality = self.quality + 1
