from .ManageWords import ManageWords

# Classe permettant de mettre en majuscule les mots
class Uppercase(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def convert_to_upper(self):
        return [word.upper() for word in self.words]

    def run(self):
        return self.convert_to_upper()
