from classes.ItemService import ItemService
from classes.Item import Item

class BackstageService:

    @staticmethod
    def set_item_quality(item, q_value):
        if ItemService.is_item_back_stage(item):
            return ItemService.set_quality_in_range(item, q_value)

    @staticmethod
    def increase_item_quality(item, val_to_add):
        return BackstageService.set_item_quality(item, item.quality + val_to_add)



print(BackstageService.increase_item_quality( Item("Backstage passes to johny", 50, 50), 3))