from classes.ItemService import ItemService


class BackstageService:
    """
        this is designed only for back stage passes treatment
    """

    @staticmethod
    def set_item_quality(item, q_value):
        if ItemService.is_item_back_stage(item):
            return ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def increase_item_quality(item, val_to_add):
        return BackstageService.set_item_quality(item, item.quality + val_to_add)

    @staticmethod
    def update_item_quality(item):
        ItemService.reduce_item_sell_in(item)
        if item.sell_in in range(6, 11):
            BackstageService.increase_item_quality(item, 2)
            return item.quality
        elif item.sell_in in range(0, 6):
            BackstageService.increase_item_quality(item, 3)
            return item.quality
        elif item.sell_in < 0:
            BackstageService.set_item_quality(item, 0)
            return item.quality
        else:
            BackstageService.increase_item_quality(item, 1)
            return item.quality
