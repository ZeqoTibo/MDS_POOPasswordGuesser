import itertools
import unidecode


def password_guesser():
    # Permet d'avoir toutes les combinaisons possibles d'un seul mot
    # test = itertools.permutations(text, len(text))
    # print(list(test))
    array = []
    listpwd = []
    options = []
    print("Veuillez saisir un prénom : ")
    prenom = input()
    array.append(prenom)
    print("Veuillez saisir le prenom de votre chien : ")
    chien = input()
    array.append(chien)
    print("Veuillez saisir une date : ")
    date = input()
    array.append(date)
    print("Que souhaitez vous comme options ? (FullMajuscule => maj, FullMinuscule => min, FullL33T => leet :")
    option = input()
    options.append(option)
    # On récupère la longueur de mon tableau contenant le prenom, le nom de chien et la date
    lenghtarray = len(array)
    allinfo = []
    print(array)
    for opt in options:
        match opt:
            case "maj":
                print("Full majuscule")
                indent = 0
                for val in array:
                    array[indent] = val.upper()
                    indent = indent + 1
            case "min":
                print("Full minuscule")
                indent = 0
                for val in array:
                    array[indent] = val.lower()
                    indent = indent + 1
            case "firstMin":
                print("Première majuscule")
                indent = 0
                for val in array:
                    array[indent] = val.capitalize()
                    indent = indent + 1
            case "noAccent":
                print("Sans accent")
                indent = 0
                for val in array:
                    array[indent] = unidecode.unidecode(val)
                    indent = indent + 1
            case "leet":
                print("Full l33t")
            case _:
                print("Ya r")

    # Pour chaque élément de mon tableau
    for i in range(lenghtarray):
        tabpermut = itertools.permutations(array, i + 1)
        allinfo = allinfo + list(tabpermut)

    tabinfos = list(allinfo)
    for tabinfo in tabinfos:
        listpwd.append(''.join(tabinfo))

    print(listpwd)


password_guesser()
