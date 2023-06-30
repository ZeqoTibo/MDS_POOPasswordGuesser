from .ManageWords import ManageWords


# Classe permettant de mettre en minuscule les mots
class Lowercase(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def convert_to_lower(self):
        return [word.lower() for word in self.words]

    def run(self):
        return self.convert_to_lower()
