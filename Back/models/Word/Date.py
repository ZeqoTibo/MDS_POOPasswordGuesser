from .ManageWords import ManageWords
from .DateCustom.NumberDate import NumberDate
from .DateCustom.NameMonthDate import NameMonthDate
from datetime import datetime


class Date(ManageWords):
    def __init__(self, words):
        self.words = words
        super().__init__(words)

    @staticmethod
    def check_date_format(word):
        try:
            datetime.fromisoformat(word)
            return True
        except ValueError:
            return False

    def run(self):
        for word in self.words:
            if Date.check_date_format(word):
                resultNumber = NumberDate(word).run()
                resultNameMonth = NameMonthDate(word).run()
                result = resultNumber + resultNameMonth
                self.words.remove(word)
                return result
