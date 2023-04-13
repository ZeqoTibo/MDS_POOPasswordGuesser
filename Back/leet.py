import itertools


class ManageLeet:
    associative = {}

    def __init__(self, words):
        self.words = words
        self.possibilities = self.run()

    def to_leet_word(self, word):
        for letter in word:
            if letter in self.associative:
                word = word.replace(letter, self.associative[letter])
        return word

    def run(self):
        leet_words = []

        for word in self.words:
            leet_words.append(self.to_leet_word(word))
        return leet_words


class GetLeetMaj(ManageLeet):
    associative = {
        "A": "4",
        "E": "3",
        "I": "1",
        "O": "0",
        "L": "1",
        "S": "5",
        "B": "8",
        "T": "7",
        "Z": "2",
        "G": "6"
    }

    def __init__(self, words):
        super().__init__(words)


class GetLeetMin(ManageLeet):
    associative = {
        "a": "4",
        "e": "3",
        "i": "1",
        "o": "0",
        "l": "1",
        "s": "5",
        "b": "8",
        "t": "7",
        "z": "2",
        "g": "6"
    }

    def __init__(self, words):
        super().__init__(words)
