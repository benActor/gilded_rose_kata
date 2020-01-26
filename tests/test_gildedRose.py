import unittest
from classes.gildedRose import GildedRose


class test_GildedRose(unittest.TestCase):
    def test_can_get_time_in_right_format(self):
        my_time = "00:23:45"
        self.assertTrue(GildedRose.time_in_right_format(my_time))

    def test_can_get_end_of_the_day(self):
        my_time = "00:00:00"

        self.assertTrue(GildedRose.is_end_of_the_day(my_time))

        self.assertFalse(GildedRose.is_end_of_the_day("14:25:33"))


if __name__ == '__main__':
    unittest.main()
