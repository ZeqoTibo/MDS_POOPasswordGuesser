import itertools

from words import GetMaj, GetMin, GetAccent, GetFirstMaj
from leet import GetLeetMin, GetLeetMaj


class Engine:

    def __init__(self, words, options):
        self.options = options
        self.words = words
        self.array_possibilities = []
        self.run()

    def run(self):
        if self.options["leet_min"]:
            self.array_possibilities.append(GetLeetMin(self.words).possibilities)
        if self.options["leet_maj"]:
            self.array_possibilities.append(GetLeetMaj(self.words).possibilities)
        if self.options["maj"]:
            self.array_possibilities.append(GetMaj(self.words).possibilities)
        if self.options["min"]:
            self.array_possibilities.append(GetMin(self.words).possibilities)
        if self.options["accent"]:
            self.array_possibilities.append(GetAccent(self.words).possibilities)
        if self.options["first_maj"]:
            self.array_possibilities.append(GetFirstMaj(self.words).possibilities)

    def get_possibilities(self):
        newTab = []
        allinfo = []
        listpwd = []
        # on boucle pour tout mettre dans un seul tableau
        for i in e.array_possibilities:
            newTab.extend(i)
        # on boucle pour avoir toutes les combinaisons possibles
        for i in range(len(newTab)):
            tabpermut = itertools.permutations(newTab, i + 1)
            allinfo = allinfo + list(set(tabpermut))
        tabinfos = list(set(allinfo))
        for tabinfo in tabinfos:
            listpwd.append(''.join(tabinfo))
        print(listpwd)
        return listpwd


options = {
    "leet_min": False,
    "leet_maj": False,
    "maj": False,
    "min": False,
    "accent": False,
    "first_maj": True
}

words = [
    "toto",
    "ALAMBIC",
]

e = Engine(words, options)
e.get_possibilities()
