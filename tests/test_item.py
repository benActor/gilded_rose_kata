import unittest
from classes.Item import Item


class TestItem(unittest.TestCase):
    def test_canInstantiateItem(self):
        item = Item("Sulfuras", 50, 80)

        self.assertTrue(hasattr(item, "sell_in"))

        self.assertTrue(hasattr(item, "quality"))

        self.assertTrue(hasattr(item, "name"))



if __name__ == '__main__':
    unittest.main()
