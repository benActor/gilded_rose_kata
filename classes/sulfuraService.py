from classes.ItemService import ItemService


class SulfuraService:
    """
        to handle the update of Sulfuras items
    """

    @staticmethod
    def set_item_quality(item):
        if ItemService.is_item_sulfuras(item):
            item.quality = 80
            return item.quality

    @staticmethod
    def update_item(item):
        SulfuraService.set_item_quality(item)
        ItemService.reduce_item_sell_in(item)
        return item.quality, item.sell_in
