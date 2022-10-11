lista = range(10)


def zad_4(liczby):
    nowa = []
    for index, liczba in enumerate(liczby):
        if (index % 2 == 0):
            nowa.append(liczba)
    return nowa


print(zad_4(lista))
