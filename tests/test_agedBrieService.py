import unittest
from classes.Item import Item
from classes.ItemService import ItemService
from classes.agedBrieService import AgedBrieService


class TesAgedBrieService(unittest.TestCase):
    def test_can_set_agedBrie_quality(self):
        item = Item("Aged Brie", 25, 30)
        q_value = -10

        self.assertTrue(AgedBrieService.set_item_quality(item, q_value) == 0)

        self.assertTrue(AgedBrieService.increase_item_quality(item, 100) < 50)

    def test_can_update_agedBrie_items(self):
        item = Item("Aged Brie", 20, 30)
        expected_quality = item.quality + 1
        sell_in_expected = item.sell_in - 1
        self.assertTrue(AgedBrieService.update_item(item) == (expected_quality, sell_in_expected))




if __name__ == '__main__':
    unittest.main()
