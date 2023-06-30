import itertools

from .ManageWords import ManageWords


class Leet(ManageWords):
    def __init__(self, words):
        super().__init__(words)

    def convert_to_leet(self):
        leet_dict = {
            'a': '4',
            'b': '8',
            'e': '3',
            'l': '1',
            'i': '1',
            'o': '0',
            's': '5',
            't': '7',
            'z': '2',
            'g': '6',
            'A': '4',
            'B': '8',
            'E': '3',
            'L': '1',
            'I': '1',
            'O': '0',
            'S': '5',
            'T': '7',
            'Z': '2',
            'G': '6'
        }
        leet_words = []
        for word in self.words:
            leet_word = ''
            leet_chars = []
            for char in word:
                if char in leet_dict:
                    leet_chars.append([char, leet_dict[char]])
                else:
                    leet_chars.append([char])
            possibility = itertools.product(*leet_chars)
            for possibility in possibility:
                leet_words.append(''.join(possibility))

        return leet_words

    def run(self):
        return self.convert_to_leet()
