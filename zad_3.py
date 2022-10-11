lista = range(10)


def zad_3(liczby):
    nowa = []
    for liczba in liczby:
        if liczba % 2 == 0:
            nowa.append(liczba)
    return nowa


print(zad_3(lista))
