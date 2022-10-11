lista = [1, 2, 3, 4, 5]


def zad_2_for(liczby):
    nowa = []
    for liczba in liczby:
        nowa.append(liczba * 2)
    return nowa


def zad_2_skladana(liczby):
    return [liczba * 2 for liczba in liczby]


print(zad_2_for(lista))
print(zad_2_skladana(lista))
