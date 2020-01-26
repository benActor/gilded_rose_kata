from classes.ItemService import ItemService
class SulfuraService:

    @staticmethod
    def set_item_quality(item):
        if ItemService.is_item_sulfuras(item):
            item.quality = 80
            return item.quality

    @staticmethod
    def update_item

