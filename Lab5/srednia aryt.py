import math as m
import numpy as np

matrix = []
with open("australian.dat", "r") as file:
    matrix = [list(map(lambda a: float(a), line.split())) for line in file]

matrix2 = [x[:14] for x in matrix]

def srednia_aryt(lista):
    suma = 0
    for x in lista:
        suma += x
    return float(suma/(float(len(lista))))


def wariancja(lista):
    srednia = srednia_aryt(lista)
    suma = 0
    for x in lista:
        suma+=(x-srednia)**2
    return float(suma/(float(len(lista))))


def odchylenie(lista):
    return m.sqrt(wariancja(lista))

print("pierwsze 14 cyfr z australii")
print("średnia")
print(srednia_aryt(matrix2[0]))
print("wariancja")
print(wariancja(matrix2[0]))
print("odchylenie")
print(odchylenie(matrix2[0]))
print("---------------")
print("z ostatnim elementem")
print("średnia")
print(srednia_aryt(matrix[0]))
print("wariancja")
print(wariancja(matrix[0]))
print("odchylenie")
print(odchylenie(matrix[0]))
print("---------------")

# popraw
def srednia_aryt_wektorowo(lista):
    ones = np.ones((len(lista),1))
    return float(1/len(lista))*np.dot(np.array(lista),ones)[0]

def wariancja_wektorowo(lista):
    srednia = srednia_aryt_wektorowo(lista)
    ones = np.ones((1,len(lista)))*srednia
    minus = np.array(lista) - ones
    return float(1/len(lista))*np.dot(minus[0],minus[0].T)

def odchylenie_std_wektorowo(lista):
    return m.sqrt(wariancja_wektorowo(lista))

print(srednia_aryt_wektorowo(matrix2[0]))
print(wariancja_wektorowo(matrix2[0]))
print(odchylenie_std_wektorowo(matrix2[0]))



