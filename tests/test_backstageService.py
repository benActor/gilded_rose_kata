import unittest
from classes.Item import Item
from classes.backStageService import BackstageService


class Test_BackstageService(unittest.TestCase):
    def can_back_stage_item_quality(self):
        item = Item("Backstage passes to johny", 25, 30)
        q_value = 100

        self.assertTrue(BackstageService.set_item_quality(item, q_value) == 50)

    def can_increase_backstage_item_quality(self):
        item = Item("Backstage passes to johny", 50, 20)
        value_to_add = 3

        self.assertTrue(BackstageService.increase_item_quality(item, value_to_add) == item.quality + value_to_add)


if __name__ == '__main__':
    unittest.main()
