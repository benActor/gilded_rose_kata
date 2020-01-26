import unittest
from classes.gildedRose import GildedRose
from classes.Item import Item
from classes.ItemService import ItemService


class test_GildedRose(unittest.TestCase):
    def test_can_get_time_in_right_format(self):
        my_time = "00:23:45"
        self.assertTrue(GildedRose.time_in_right_format(my_time))

    def test_can_get_end_of_the_day(self):
        my_time = "00:00:00"

        self.assertTrue(GildedRose.is_end_of_the_day(my_time))

        self.assertFalse(GildedRose.is_end_of_the_day("14:25:33"))

    def test_can_update_items(self):
        current_time = "00:00:00"
        items = [Item("Sulfuras", 20, 40), Item("Conjured", 25, 60), Item("Backstage passes to johny", 2, 46)]

        expected_first_item = Item("Sulfuras", 19, 80)
        expected_second_item = Item("Conjured", 24, 50)

        new_items_list = GildedRose.update_items(items, current_time)

        self.assertTrue(ItemService.are_item_equal(new_items_list[0], expected_first_item))

        self.assertTrue(ItemService.are_item_equal(new_items_list[1], expected_second_item))


if __name__ == '__main__':
    unittest.main()
