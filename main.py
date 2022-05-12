import random

prefix = ["The story", "The blade", "The sword", "The legendary weapon", "The journey", "The mountain",
          "The legend", "The mother", "The father", "The teacher", "The friend"
          ]

suffix = ["the beginning", "your mom", "legends", "the mountain", "gloom", "doom", "death", "dancing!", "the rats",
          "the scammer", "the pitiful"
          ]


def generateur_de_noms2():
    list_random = []
    for x in range(10):

        prefix_random = random.choice(prefix)
        while (prefix_random in list_random) == True:
            prefix_random = random.choice(prefix)

        list_random.append(prefix_random)

        suffix_random = random.choice(suffix)
        while (suffix_random in list_random) == True:
            suffix_random = random.choice(suffix)

        list_random.append(suffix_random)

        print(prefix_random + " of " + suffix_random)


def generateur_de_noms():

    for x in range(10):
        rnd_prf = random.choice(prefix)
        rnd_sfx = random.choice(suffix)
        print(rnd_prf + " of " + rnd_sfx)

        prefix.pop(prefix.index(rnd_prf))
        suffix.pop(suffix.index(rnd_sfx))

        return prefix, suffix


if __name__ == "__main__":
    generateur_de_noms()

    """
    :       ==  a) après une déclaration de fonction
    def patator():
                b) après un if, else ou truc comme ça 
    if patator():
                c) les boucles
    for x in range(prout):
            => tout ce qui change le niveau d'indentation        

    truc()  == fonction ou tuple
    truc[]  == tableau ou list
    truc=   == variable
    """
