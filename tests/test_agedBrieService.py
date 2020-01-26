import unittest
from classes.Item import Item
from classes.ItemService import ItemService
from classes.agedBrieService import AgedBrieService


class TesAgedBrieService(unittest.TestCase):
    def test_can_set_agedBrie_quality(self):
        item = Item("Aged Brie", 25, 30)
        q_value = -10

        self.assertTrue(AgedBrieService.set_item_quality(item, q_value) == 0)

        self.assertTrue(AgedBrieService.increase_item_quality(item, 5) == 5)




if __name__ == '__main__':
    unittest.main()
