from abc import ABC, abstractmethod


class ManageWords(ABC):
    @abstractmethod
    def __init__(self, words):
        self.words = words
        self.possibilities = self.run()

    def run(self):
        return self.transform()

    def transform(self):
        return [];
