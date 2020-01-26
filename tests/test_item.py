import unittest
from classes.Item import Item


class MyTestCase(unittest.TestCase):
    def test_canInstantiateItem(self):
        item = Item()


if __name__ == '__main__':
    unittest.main()
