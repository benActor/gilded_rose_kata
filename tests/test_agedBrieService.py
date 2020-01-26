import unittest
from classes.Item import Item
from classes.ItemService import ItemService


class TesAgedBrieService(unittest.TestCase):
    def test_can_set_agedBrie_quality(self):
        item = Item("Aged Brie", 25, 30)



if __name__ == '__main__':
    unittest.main()
