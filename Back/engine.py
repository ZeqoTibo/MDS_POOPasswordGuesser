import itertools


def get_random_string():
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
    lenghtArray = len(array)
    allinfo = []
    # Pour chaque élément de mon tableau
    for i in range(lenghtArray):
        tabpermut = itertools.permutations(array, i+1)
        allinfo = allinfo + list(tabpermut)

    tabinfos = list(allinfo)
    for tabinfo in tabinfos:
        listpwd.append(''.join(tabinfo))

    print(listpwd)


get_random_string()
