from datetime import datetime
import re
from classes.ItemService import ItemService
from classes.sulfuraService import SulfuraService
from classes.conjuredService import ConjuredService
from classes.backStageService import BackstageService
from classes.standardItemService import StandardItemService
from classes.agedBrieService import AgedBrieService


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
    def update_items(items):
        if GildedRose.is_end_of_the_day(datetime.now().strftime('%H:%M:%S')):
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


if __name__ == '__main__':
    items = []
    GildedRose.update_items(items)


