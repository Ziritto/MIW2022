import math as m

miasta = ["Białystok", "Olsztyn", "Warszawa", "Kraków", "Gdańsk"]

print(list(map(lambda a:a[0:3], miasta)))

matrix = []

with open("australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]

print("----------------------------------")
print(matrix)
print("----------------------------------")
def euklides(l1, l2):
    suma = 0
    for i in range(max(len(l1), len(l2)) - 1):
        suma += (l1[i] - l2[i]) ** 2
    return m.sqrt(suma)

print("----------------------------------")
print(euklides(matrix[0],matrix[1]))
print(euklides(matrix[0],matrix[2]))
print(euklides(matrix[0],matrix[3]))
print("----------------------------------")


def grupo_australia(lista, index, poczontek):
    wynik = dict()
    y = lista[poczontek]
    for x in range(1, len(lista)):
        decyzja = lista[x][index]
        if decyzja in wynik.keys():
            wynik[decyzja].append(euklides(y, lista[x]))
        else:
            wynik[decyzja] = [euklides(y, lista[x])]
    return wynik

print("----------------------------------")
zmienna = grupo_australia(matrix,14,0)
print(zmienna)
print(euklides(matrix[0],matrix[5]))
print(euklides(matrix[0],matrix[10]))
print(euklides(matrix[0],matrix[20]))
print("----------------------------------")


def k_nn(lista, index, somsiad):
    wynik = dict()
    for x in range(0, len(lista)):
        decyzja = lista[x][index]
        if decyzja in wynik.keys():
            wynik[decyzja].append(euklides(somsiad, lista[x]))
        else:
            wynik[decyzja] = [euklides(somsiad, lista[x])]
    return wynik


def k_nn_lista(lista, index, somsiad):
    wynik = []
    for x in range(0, len(lista)):
        decyzja = lista[x][index]
        wynik.append((decyzja, euklides(somsiad, lista[x])))
    return wynik


test = k_nn(matrix, 14, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
print("--------------------")
print(test[0][:3])
print(test[1][:3])
print("--------------------")
test[0].sort()
test[1].sort()
print(test[0][:3])
print(sum(test[0][:3]))
print("--------------------")
print(test[1][:3])
print(sum(test[1][:3]))
print("----------------------------------------------------------------------------------------------------")
# nowe

def grupuj(lista, a):
    wynik = dict()
    for element in lista:
        decyzja = element[0]
        if decyzja in wynik.keys():
            wynik[decyzja].append(element[1])
        else:
            wynik[decyzja] = [element[1]]
    for klucz in wynik.keys():
        wynik[klucz].sort()
    for klucz in wynik.keys():
        suma = 0
        for ele in wynik[klucz][:a]:
            suma += ele
        wynik[klucz] = suma
    return wynik


grupy = grupuj(k_nn_lista(matrix, 14, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), 5)
print(grupy[0])
print(grupy[1])


def decyzja(slownik):
    klucze = list(slownik.keys())
    ilosc = 1
    klasa = klucze[0]
    minimum = slownik[klucze[0]]
    for key in klucze[1:]:
        if minimum > slownik[key]:
            minimum = slownik[key]
            klasa = key
            ilosc = 1
        elif minimum == slownik[key]:
            ilosc += 1
    if ilosc > 1:
        return
    return klasa

test_zly = {0.0: 4, 1.0: 4, 2.0: 6}
test = {0.0: 4, 1.0: 4, 2.0: 3}
print("Decyzja:", decyzja(test_zly))
print("Decyzja:", decyzja(test))