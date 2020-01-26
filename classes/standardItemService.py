from classes.ItemService import ItemService

class StandardItemService:

    """"
    for non special items that is items that are not present in the special item list
    """

    @staticmethod
    def set_item_quality(item, q_value):
        if not ItemService.is_special_item(item):
           ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def reduce_item_quality_by(item, value):
        if not ItemService.is_special_item(item):
            StandardItemService.set_item_quality(item, item.quality - value)
            return item.quality

    @staticmethod
    def update_item_quality(item):
        ItemService.reduce_item_sell_in(item)
        StandardItemService.reduce_item_quality_by(item, 1)
        return item.quality, item.sell_in



