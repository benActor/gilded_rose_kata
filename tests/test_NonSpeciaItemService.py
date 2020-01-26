import unittest
from classes.nonSpecialItemService import NonSpecialItemService
from classes.Item import Item

class NonSpecialItemService(unittest.TestCase):


    def can_set_item_quality(self):
        item = Item("passes to johnny", 25, 25)
        q_value = 60
        self.assertTrue(NonSpecialItemService.set_item_quality(item, q_value) < 50)

if __name__ == '__main__':
    unittest.main()
