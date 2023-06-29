from ..ManageWords import ManageWords
from datetime import datetime


class NumberDate(ManageWords):

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
    def separate_date_info(word):
        date = datetime.strptime(word, '%Y-%m-%d').date()
        day = str(date.day)
        month = str(date.month)
        year = str(date.year)
        return [day, month, year]

    def run(self):
        for word in self.words:
            if NumberDate.check_date_format(word):
                result = NumberDate.separate_date_info(word)
                if len(result) > 0:
                    self.words.extend(result)

        return self.words
