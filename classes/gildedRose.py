from datetime import datetime
import re
from classes.ItemService import ItemService
from classes.sulfuraService import SulfuraService
from classes.conjuredService import ConjuredService
from classes.backStageService import BackstageService
from classes.standardItemService import StandardItemService
from classes.agedBrieService import AgedBrieService

from classes.Item import Item


class GildedRose:
    items = []

    @staticmethod
    def time_in_right_format(my_time):
        if bool(re.match(r"\d\d:\d\d:\d\d", my_time)) and len(my_time) == 8:
            return True
        return False

    @staticmethod
    def is_end_of_the_day(my_time):
        return GildedRose.time_in_right_format(my_time) and my_time == "00:00:00"

    @staticmethod
    def update_items(items, current_time):
        if GildedRose.is_end_of_the_day(current_time):
            for item in items:
                if ItemService.is_item_conjured(item):
                    ConjuredService.update_quality(item)
                elif ItemService.is_item_back_stage(item):
                    BackstageService.update_item_quality(item)
                elif ItemService.is_item_sulfuras(item):
                    SulfuraService.update_item(item)
                elif ItemService.is_aged_brie(item):
                    AgedBrieService.update_item(item)
                elif not ItemService.is_special_item(item):
                    StandardItemService.update_item_quality(item)
            return items


if __name__ == '__main__':
    items = [Item("Sulfuras", 20, 40), Item("Conjured", 25, 60), Item("Backstage passes to johny", 2, 46)]
    # GildedRose.update_items(items, datetime.now().strftime('%H:%M:%S'))
    GildedRose.update_items(items, "00:00:00")

    print(items[1])
    print(ItemService.are_item_equal(items[1], Item("Conjured", 24, 50)))




