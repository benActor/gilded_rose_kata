import unittest
from classes.nonSpecialItemService import NonSpecialItemService
from classes.Item import Item


class Test_NonSpecialItemService(unittest.TestCase):

    def test_can_set_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        q_value = 60
        self.assertTrue(NonSpecialItemService.set_item_quality(item, q_value) < 50)

    def test_can_reduce_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        value = 1
        self.assertTrue(NonSpecialItemService.reduce_item_quality_by(item, value) == 24)


if __name__ == '__main__':
    unittest.main()
