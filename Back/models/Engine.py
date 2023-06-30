from itertools import combinations, permutations
from .Word.Uppercase import Uppercase
from .Word.Lowercase import Lowercase
from .Word.Accent import Accent
from .Word.Leet import Leet
from .Word.Capitalize import ToCapitalize
from .Word.Date import Date
from .Word.SpecialChar import SpecialChar


class Engine:

    def __init__(self, words, options=[]):
        self._words = words
        self.options = options
        self.possibilities = []
        self.passwords = self.run()

    def run(self):
        self._process_options()
        self._permute_and_combine_list()
        return self._fromArrayToString()

    def _process_options(self):
        if 'date' in self.options:
            self._update_words(Date(self.get_words()).possibilities)
        if 'upper' in self.options:
            self._update_words(Uppercase(self.get_words()).possibilities)
        if 'lower' in self.options:
            self._update_words(Lowercase(self.get_words()).possibilities)
        if 'capitalize' in self.options:
            self._update_words(ToCapitalize(self.get_words()).possibilities)
        if 'leet' in self.options:
            self._update_words(Leet(self.get_words()).possibilities)
        if 'accent' in self.options:
            self._update_words(Accent(self.get_words()).possibilities)
        if 'char' in self.options:
            self._update_words(SpecialChar().get_special_characters())
        return self.get_words()

    def _update_words(self, new_words):
        self._words = list(set(self._words + new_words))

    def _permute_and_combine_list(self):
        limit = 4 if len(self._words) > 5 else len(self._words) + 1
        for i in range(1, limit):
            for combo in combinations(self._words, i):
                for perm in permutations(combo):
                    self.possibilities.append(perm)

    def _fromArrayToString(self):
        result = []
        for item in self.possibilities:
            result.append(''.join(item))
        return result

    def get_words(self):
        return self._words

    def set_words(self, new_words):
        self._words = new_words
