from .ManageWords import ManageWords
from unidecode import unidecode


# Classe permettant d'enlever les accents des mots
class Accent(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def delete_all_accent(self):
        return [unidecode(word) for word in self.words]

    def run(self):
        return self.delete_all_accent()
