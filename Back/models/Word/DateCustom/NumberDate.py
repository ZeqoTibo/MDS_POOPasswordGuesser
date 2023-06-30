from ..ManageWords import ManageWords
from datetime import datetime


class NumberDate(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def _separate_date_info(word):
        date = datetime.strptime(str(word), '%Y-%m-%d').date()
        day = str(date.day)
        month = str(date.month)
        year = str(date.year)
        return [day, month, year]

    def run(self):
        result = NumberDate._separate_date_info(self.words)
        if len(result) > 0:
            return result
