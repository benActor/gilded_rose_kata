from classes.Item import Item


class ItemService:

    special_items = {
        "sulfuras": "Sulfuras",
        "back_stage": "Backstage passes",
        "aged_brie": "Aged Brie",
        "conjured": "Conjured"
    }

    @staticmethod
    def item_has_given_attributte(item, attribute):
        if hasattr(item, attribute):
            return True
        raise AttributeError('an attribute {} must be defined for the item'.format(attribute))

    @staticmethod
    def is_item_valid(item):
        if type(item) is Item:
            return True
        raise TypeError("item should be of type item")

    @staticmethod
    def is_entry_value_integer(value):
        if not type(value) is int:
            raise TypeError('The value must be an integer')
        return True

    @staticmethod
    def reduce_item_sell_in(item):
        if ItemService.is_item_valid(item) and ItemService.item_has_given_attributte(item, 'sell_in'):
            if ItemService.is_entry_value_integer(item.sell_in):
                item.sell_in -= 1
                return item.sell_in

    @staticmethod
    def is_special_item(item):
        if ItemService.is_item_valid(item) and ItemService.item_has_given_attributte(item, "name"):
            for item_type in ItemService.special_items:
                if ItemService.special_items[item_type] in item.name:
                    return True
            return False


    @staticmethod
    def is_aged_brie(item):
        return ItemService.special_items["aged_brie"] in item.name

    @staticmethod
    def is_item_sulfuras(item):
        return ItemService.special_items["sulfuras"] in item.name







