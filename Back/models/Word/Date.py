from .ManageWords import ManageWords
from .DateCustom.NumberDate import NumberDate
from .DateCustom.NameMonthDate import NameMonthDate


class Date(ManageWords):
    def __init__(self, words):
        self.words = words
        super().__init__(words)

    def run(self):
        print(NumberDate(self.words).run())
        print(NameMonthDate(self.words).run())
        return 'result.run()'
