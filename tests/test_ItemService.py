import unittest
from classes.ItemService import ItemService

class TestItemService(unittest.TestCase):

    def test_can_detect_items_of_valid_type(self):

        self.assertFalse(ItemService.is_item_valid("item"))




if __name__ == '__main__':
    unittest.main()
