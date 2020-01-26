import unittest
from classes.ItemService import ItemService
from classes.Item import Item

class TestItemService(unittest.TestCase):

    def test_can_detect_items_of_valid_type(self):

        self.assertRaises(TypeError,  ItemService.is_item_valid, "item")

        self.assertTrue(ItemService.is_item_valid, Item("Sulfuras", 20, 80))

    def test_can_reduce_item_sell_in(self):
        item = Item("Sulfuras", 20, 80)
        value = 1
        expected_value = item.sell_in - value
        self.assertTrue(ItemService.reduce_item_sell_in_by_value(item, value) == expected_value )






if __name__ == '__main__':
    unittest.main()
