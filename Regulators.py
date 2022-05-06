
from random import randrange


def Rearranger():
    Words = input(" ")
    print(Words)
    Listy = Words.split()
    print(Listy)

    for each in Listy:
        Lister = (len(Listy))
        for each in Listy:
            x = randrange(0, Lister)
            y = randrange(0, Lister)
            Listy[x],Listy[y] = Listy[y],Listy[x]
        print(Listy)
        return " ".join(Listy)

Cows = Rearranger()
print(Cows)



