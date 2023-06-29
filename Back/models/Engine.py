from itertools import combinations, permutations
from .Word.Uppercase import Uppercase
from .Word.Lowercase import Lowercase
from .Word.Accent import Accent
from .Word.Leet import Leet
from .Word.Capitalize import Capitalize
from .Word.Date import Date


class Engine:

    def __init__(self, words, options=[]):
        self.words = words
        self.options = options
        self.possibilities = []
        self.passwords = self.run()

    def run(self):
        if 'upper' in self.options:
            self.updateWords(Uppercase(self.words).possibilities)
        if 'lower' in self.options:
            self.updateWords(Lowercase(self.words).possibilities)
        if 'capitalize' in self.options:
            self.updateWords(Capitalize(self.words).possibilities)
        if 'accent' in self.options:
            self.updateWords(Accent(self.words).possibilities)
        if 'leet' in self.options:
            self.updateWords(Leet(self.words).possibilities)
        if 'date' in self.options:
            self.updateWords(Date(self.words).possibilities)

        # print("Nombres de mots transformés : " + str(len(self.words)))
        self.permute_and_combine_list()
        print(self.words)
        # print(self.fromArrayToString())
        return len(self.words)
        # return self.fromArrayToString()

    def updateWords(self, newWords):
        self.words = list(set(self.words + newWords))

    def permute_and_combine_list(self):
        limit = 6 if len(self.words) > 5 else len(self.words) + 1
        for i in range(1, limit):
            for combo in combinations(self.words, i):
                for perm in permutations(combo):
                    self.possibilities.append(perm)

    def fromArrayToString(self):
        result = []
        for item in self.possibilities:
            result.append(''.join(item))
        return result