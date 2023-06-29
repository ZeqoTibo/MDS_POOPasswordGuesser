from ..ManageWords import ManageWords
from datetime import datetime


class NameMonthDate(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    @classmethod
    def check_date_format(cls, word):
        try:
            datetime.fromisoformat(word)
            return True
        except ValueError:
            return False

    @staticmethod
    def get_name_month(word):
        date = datetime.strptime(word, '%Y-%m-%d').date()
        month = str(date.month)

        month_names = [
            'janvier', 'février', 'mars', 'avril', 'mai', 'juin',
            'juillet', 'août', 'septembre', 'octobre', 'novembre', 'décembre'
        ]

        try:
            month_number = int(month)
            if 1 <= month_number <= 12:
                month_name = month_names[month_number - 1]
                return month_name
        except ValueError:
            pass

        return None

    def run(self):
        for word in self.words:
            if NameMonthDate.check_date_format(word):
                result = NameMonthDate.get_name_month(word)
                if len(result) > 0:
                    self.words.extend(result)

        return self.words
