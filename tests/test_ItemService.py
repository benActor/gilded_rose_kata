import unittest
from classes.ItemService import ItemService
from classes.Item import Item

class TestItemService(unittest.TestCase):

    def test_can_detect_items_of_valid_type(self):

        self.assertRaises(TypeError,  ItemService.is_item_valid, "item")

        self.assertTrue(ItemService.is_item_valid, Item("Sulfuras", 20, 80))





if __name__ == '__main__':
    unittest.main()
