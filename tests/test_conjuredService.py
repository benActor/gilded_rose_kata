import unittest
from classes.Item import Item
from classes.conjuredService import ConjuredService


class Test_ConjuredService(unittest.TestCase):
    def test_can_set_conjured_item_quality(self):
        item = Item("Conjured", 25, 35)
        q_value = 100

        expected_quality = 50

        self.assertTrue(ConjuredService.set_item_quality(item, q_value) == expected_quality)

    def test_can_reduce_conjured_item_quality(self):
        item = Item("Conjured", 25, 35)

        value_to_reduce = 2

        expected_quality = 33

        self.assertTrue(ConjuredService.reduce_item_quality(item, value_to_reduce) == expected_quality)

    def test_can_update_conjured_items_quality(self):
        item = Item("Conjured", 25, 35)

        expected_quality = 33

        self.assertTrue(ConjuredService.update_quality(item) == expected_quality)






if __name__ == '__main__':
    unittest.main()
