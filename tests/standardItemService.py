import unittest
from classes.standardItemService import StandardItemService
from classes.Item import Item


class Test_StandardItemService(unittest.TestCase):

    def test_can_set_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        q_value = 60
        self.assertTrue(StandardItemService.set_item_quality(item, q_value) < 50)

    def test_can_reduce_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        value = 1
        self.assertTrue(StandardItemService.reduce_item_quality_by(item, value) == 24)

    def test_can_update_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        expected_quality = item.quality - 1
        expected_sell_in = item.sell_in - 1
        self.assertTrue(StandardItemService.update_item_quality(item) == (expected_quality, expected_sell_in))



if __name__ == '__main__':
    unittest.main()
