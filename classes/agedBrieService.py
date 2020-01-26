from classes.ItemService import ItemService

class AgedBrieService:
    @staticmethod
    def set_item_quality(item , q_value):
        if ItemService.is_aged_brie(item):
            return ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def increase_item_quality(item, value):
        return AgedBrieService.set_item_quality(item, item.quality + value)


