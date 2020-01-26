import unittest
from classes.ItemService import ItemService
from classes.Item import Item


class TestItemService(unittest.TestCase):

    def test_can_detect_items_of_valid_type(self):
        self.assertRaises(TypeError, ItemService.is_item_valid, 'item')

        self.assertTrue(ItemService.is_item_valid, Item('Sulfuras', 20, 80))

    # this test check if an entry is of type integer
    def test_can_identify_valid_entry_value(self):
        self.assertRaises(TypeError, ItemService.is_entry_value_integer, 'a string')

        self.assertTrue(ItemService.is_entry_value_integer, 2)

    # should be able to reduce the sell_in attribute by 1
    def test_can_reduce_item_sell_in(self):
        item = Item("Sulfuras", 20, 80)
        item2 = Item("AgedBrie", "20", 50)

        expected_value = item.sell_in - 1

        self.assertTrue(ItemService.reduce_item_sell_in(item) == expected_value)

        self.assertRaises(TypeError, ItemService.reduce_item_sell_in, item2)

    # raise an exeption if we try to access an undefined attribute
    def test_attribute_is_defined(self):
        self.assertTrue(ItemService.item_has_given_attributte(Item('concert', 12, 30), 'name'))

        self.assertRaises(AttributeError, ItemService.item_has_given_attributte, Item('concert', 12, 30), 'price')

    def test_can_identify_special_items(self):
        self.assertTrue(ItemService.is_special_item(Item('Backstage passes to johny concert', 50, 30)))

        self.assertFalse(ItemService.is_special_item(Item('passes to john legend', 25, 50)))

    def test_identify_aged_brie_type(self):
        item = Item('Aged Brie', 25, 50)

        item2 = Item("sulfuras", 35, 50)

        item3 = Item("conjured", 35, 50)

        item4 = Item("Backstage passes to johny concert", 35, 50)

        item5 = Item('passes to john legend', 25, 50)

        self.assertTrue(ItemService.is_aged_brie, item)

        self.assertTrue(ItemService.is_item_sulfuras, item2)

        self.assertFalse(ItemService.is_aged_brie(item2))

        self.assertTrue(ItemService.is_item_conjured, item3)

        self.assertTrue(ItemService.is_item_back_stage(item4))

        self.assertFalse(ItemService.is_item_back_stage(item5))


    def test_can_compare_two_items(self):
        item = Item('Aged Brie', 25, 50)

        item2 = Item('Aged Brie', 25, 50)

        self.assertTrue(ItemService.are_item_equal(item, item2))
if __name__ == '__main__':
    unittest.main()
