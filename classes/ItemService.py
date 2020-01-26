from classes.Item import Item

class ItemService:
    @ staticmethod
    def is_item_valid(item):
        if type(item) is Item:
            return True
        raise TypeError("item should be of type item")


