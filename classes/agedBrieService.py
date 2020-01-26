from classes.ItemService import ItemService

class AgedBrieService:
    @staticmethod
    def set_item_quality(item , q_value):
        if ItemService.is_aged_brie(item):
            return ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def increase_item_quality(item, value):
        return AgedBrieService.set_item_quality(item, item.quality + value)

    @staticmethod
    def update_item(item):
        ItemService.reduce_item_sell_in(item)
        AgedBrieService.increase_item_quality(item, 1)
        return item.quality, item.sell_in


