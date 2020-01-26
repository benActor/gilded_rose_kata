from classes.ItemService import ItemService

class StandardItemService:

    @staticmethod
    def set_item_quality(item, q_value):
        if not ItemService.is_special_item(item):
            if ItemService.is_entry_value_integer(q_value):
                if ItemService.item_has_given_attributte(item, "quality"):
                    if q_value < 0:
                        item.quality = 0
                        return item.quality
                    elif q_value > 50:
                        item.quality = 0
                        return item.quality
                    else:
                        item.quality = q_value
                        return item.quality

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



