from classes.ItemService import ItemService


class ConjuredService:
    @staticmethod
    def set_item_quality(item, q_value):
        if ItemService.is_item_conjured(item):
            return ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def reduce_item_quality(item, val_to_reduce):
        return ConjuredService.set_item_quality(item, item.quality - val_to_reduce)


