from classes.ItemService import ItemService


class ConjuredService:
    @staticmethod
    def set_item_quality(item, q_value):
        if ItemService.is_item_conjured(item):
            return ItemService.set_quality_in_range(item, q_value)


