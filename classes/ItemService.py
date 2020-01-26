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
        if ItemService.is_item_valid(item):
            return ItemService.special_items["aged_brie"] in item.name

    @staticmethod
    def is_item_sulfuras(item):
        if ItemService.is_item_valid(item):
            return ItemService.special_items["sulfuras"] in item.name

    @staticmethod
    def is_item_conjured(item):
        if ItemService.is_item_valid(item):
            return ItemService.special_items["conjured"] in item.name

    @staticmethod
    def is_item_back_stage(item):
        if ItemService.is_item_valid(item):
            return ItemService.special_items["back_stage"] in item.name

    @staticmethod
    def set_quality_in_range(item, q_value):
        if ItemService.is_entry_value_integer(q_value):
            if ItemService.item_has_given_attributte(item, "quality"):
                if q_value < 0:
                    item.quality = 0
                    return item.quality
                elif q_value > 50:
                    item.quality = 50
                    return item.quality
                else:
                    item.quality = q_value
                    return item.quality

    @staticmethod
    def are_item_equal(item1, item2):
         if ItemService.is_item_valid(item1) and ItemService.is_item_valid(item2):
             return item1.name == item2.name and item1.quality == item2.quality and item1.sell_in == item2.sell_in










