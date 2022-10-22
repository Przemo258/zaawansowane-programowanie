def zad_6(arr1: list, arr2: list) -> list:
    return [x ** 3 for x in list(dict.fromkeys(arr1 + arr2))]


print(zad_6([1, 2, 3, 4], [3, 4, 5, 6, 7]))
