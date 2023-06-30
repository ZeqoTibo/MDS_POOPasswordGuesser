from itertools import combinations, permutations
from .Word.Uppercase import Uppercase
from .Word.Lowercase import Lowercase
from .Word.Accent import Accent
from .Word.Leet import Leet
from .Word.Capitalize import Capitalize
from .Word.Date import Date
from .Word.SpecialChar import SpecialChar


class Engine:

    def __init__(self, words, options=[]):
        self._words = words
        self.options = options
        self.possibilities = []
        self.passwords = self.run()

    def run(self):
        if 'date' in self.options:
            self.update_words(Date(self.get_words()).possibilities)
        if 'upper' in self.options:
            self.update_words(Uppercase(self.get_words()).possibilities)
        if 'lower' in self.options:
            self.update_words(Lowercase(self.get_words()).possibilities)
        if 'capitalize' in self.options:
            self.update_words(Capitalize(self.get_words()).possibilities)
        if 'leet' in self.options:
            self.update_words(Leet(self.get_words()).possibilities)
        if 'accent' in self.options:
            self.update_words(Accent(self.get_words()).possibilities)
        if 'char' in self.options:
            self.update_words(SpecialChar().get_special_characters())

        self.permute_and_combine_list()
        print(self._words)
        return len(self.fromArrayToString())
        # return self.fromArrayToString()

    def update_words(self, new_words):
        self._words = list(set(self._words + new_words))

    def permute_and_combine_list(self):
        limit = 4 if len(self._words) > 5 else len(self._words) + 1
        for i in range(1, limit):
            for combo in combinations(self._words, i):
                for perm in permutations(combo):
                    self.possibilities.append(perm)

    def fromArrayToString(self):
        result = []
        for item in self.possibilities:
            result.append(''.join(item))
        return result

    def get_words(self):
        return self._words

    def set_words(self, new_words):
        self._words = new_words
