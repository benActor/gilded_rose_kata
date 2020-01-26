import unittest
from classes.gildedRose import GildedRose


class test_GildedRose(unittest.TestCase):
    def test_can_get_time_in_right_format(self):
        my_time = GildedRose.get_time_in_right_format()
        self.assertTrue(my_time)

    def test_can_get_end_of_the_day(self):
        pass


if __name__ == '__main__':
    unittest.main()
