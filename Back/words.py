from unidecode import unidecode


class ManageWords:

    def __init__(self, words):
        self.words = words
        self.possibilities = self.run()

    def run(self):
        pass


class GetMaj(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def convert_to_upper(self):
        return [word.upper() for word in self.words]

    def run(self):
        return self.convert_to_upper()


class GetMin(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def convert_to_lower(self):
        return [word.lower() for word in self.words]

    def run(self):
        return self.convert_to_lower()


class GetAccent(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def delete_all_accent(self):
        return [unidecode(word) for word in self.words]

    def run(self):
        return self.delete_all_accent()


class GetFirstMaj(ManageWords):

    def __init__(self, words):
        super().__init__(words)

    def delete_all_accent(self):
        return [word.capitalize() for word in self.words]

    def run(self):
        return self.delete_all_accent()
