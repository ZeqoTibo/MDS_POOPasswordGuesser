import itertools

REPLACE = {letter: str(index) for index, letter in enumerate('oizeasgtb')}

leet_dict = {
    'a': ['4'],
    'b': ['8'],
    'e': ['3'],
    'l': ['1'],
    'i': ['1'],
    'o': ['0'],
    's': ['5'],
    't': ['7'],
    'z': ['2'],
    'g': ['6'],
}
def generate_leet_combinations(word):
    leet_combinations = []
    for char in word:
        if char.lower() in leet_dict:
            leet_combinations.append(leet_dict[char.lower()])
        else:
            leet_combinations.append([char])
    leet_combinations = list(itertools.product(*leet_combinations))
    leet_combinations = [''.join(x) for x in leet_combinations]
    return leet_combinations
def generate_leet_combinations_for_list(words):
    leet_combinations_list = []
    for word in words:
        leet_combinations = generate_leet_combinations(word)
        leet_combinations_list.append(leet_combinations)
    return leet_combinations_list

def Leet2Combos(word):
    possibles = []
    for l in word.lower():
        ll = REPLACE.get(l, l)
        possibles.append((l,) if ll == l else (l, ll))
    return [''.join(t) for t in itertools.product(*possibles)]



def password_guesser():
    # Permet d'avoir toutes les combinaisons possibles d'un seul mot
    # test = itertools.permutations(text, len(text))
    # print(list(test))
    global isLeet
    array = []
    arrayLeet = []
    listpwd = []
    options = []
    leetTab = []
    while True:
        print("Veuillez saisir un mot, si vous souhaitez ne plus en saisir, tapez stop : ")
        inputword = input()
        if( inputword == "stop"):
            print("Vous avez arrêté la saisie de mot")
            break
        array.append(inputword)
    print("Que souhaitez vous comme options ? (FullMajuscule => maj, FullMinuscule => min, FullL33T => leet, SansAccent => noAccent, PremièreLettreMajuscule => firstMin)")
    option = input()
    options.append(option)
    lengtharray = len(array)
    allinfo = []
    isLeet = False
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
                leet_combinations_list = generate_leet_combinations_for_list(array)
                print(leet_combinations_list)
                isLeet = True
                arrayLeet = leet_combinations_list
                break
            case _:
                print("Ya r")

    if(isLeet != True):
        # Pour chaque élément de mon tableau
        print(array)
        for i in range(lengtharray):
            tabpermut = itertools.permutations(array, i + 1)
            allinfo = allinfo + list(tabpermut)
        tabinfos = list(allinfo)
        for tabinfo in tabinfos:
            listpwd.append(''.join(tabinfo))
    else:
        array = []
        for leet in arrayLeet:
            print(leet[0])
            array.append(leet[0])
            print(array)
        for i in range(lengtharray):
            tabpermut = itertools.permutations(array, i + 1)
            allinfo = allinfo + list(tabpermut)
        tabinfos = list(allinfo)
        for tabinfo in tabinfos:
            listpwd.append(''.join(tabinfo))


    print(listpwd)


password_guesser()
