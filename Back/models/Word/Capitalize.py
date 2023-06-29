from .ManageWords import ManageWords


class Capitalize(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def capitalizeWord(self):
        return [word.capitalize() for word in self.words]

    def run(self):
        return self.capitalizeWord()
