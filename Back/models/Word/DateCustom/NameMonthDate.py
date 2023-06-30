from ..ManageWords import ManageWords
from datetime import datetime


class NameMonthDate(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    @staticmethod
    def get_name_month(word):
        date = datetime.strptime(word, '%Y-%m-%d').date()
        month = str(date.month)

        month_names = [
            'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
            'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
        ]

        month_namesEN = [
            'january', 'february', 'march', 'april', 'may', 'june',
            'july', 'august', 'september', 'october', 'november', 'december'
        ]

        try:
            month_number = int(month)
            if 1 <= month_number <= 12:
                month_name = month_names[month_number - 1]
                month_nameEN = month_namesEN[month_number - 1]
                result = [month_nameEN] + [month_name]
                return result
        except ValueError:
            pass

        return None

    def run(self):
        result = NameMonthDate.get_name_month(self.words)
        if len(result) > 0:
            return result
