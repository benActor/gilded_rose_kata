from datetime import datetime
import re


class GildedRose:

    @staticmethod
    def get_time_in_right_format():
        my_time = datetime.now().strftime('%H:%M:%S')
        if bool(re.match(r"\d\d:\d\d:\d\d", my_time)) and len(my_time) == 8:
            return True
        return False


