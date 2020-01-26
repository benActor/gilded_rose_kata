from classes.Item import Item


class ItemService:
    @staticmethod
    def is_item_valid(item):
        if type(item) is Item:
            return True
        raise TypeError("item should be of type item")

    @staticmethod
    def is_entry_value_integer(value):
        if not type(value) is int:
            raise TypeError("The value must be an integer")
        return True

    @staticmethod
    def reduce_item_sell_in(item):
        if ItemService.is_item_valid(item):
            if ItemService.is_entry_value_integer(item.sell_in):
                item.sell_in -= 1
                return item.sell_in


