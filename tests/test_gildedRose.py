import unittest
from classes.gildedRose import GildedRose
from classes.Item import Item


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

        expected_output = ["Sulfuras", 19, 80, "Conjured", 24, 50, "Backstage passes to johny", 1, 49]

        self.assertTrue(GildedRose.update_items(items, current_time) == expected_output)


if __name__ == '__main__':
    unittest.main()
