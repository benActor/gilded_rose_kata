import unittest
from classes.Item import Item
from classes.sulfuraService import SulfuraService



class Test_Sulfuras_service(unittest.TestCase):
    def test_can_set_sulfuras_item_quality(self):
        item = Item("Sulfuras", 25, 50)

        self.assertTrue(SulfuraService.set_item_quality(item) == 80)


if __name__ == '__main__':
    unittest.main()
