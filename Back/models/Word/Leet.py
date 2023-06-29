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
            for char in word:
                if char.lower() in leet_dict:
                    leet_word += leet_dict[char.lower()]
                else:
                    leet_word += char
            leet_words.append(leet_word)
        return leet_words

    def run(self):
        return self.convert_to_leet()
