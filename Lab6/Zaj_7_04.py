import math as m
import numpy as np


def kowar(matrix):
    return np.dot(matrix.T, matrix)


def macierz_odwrot(matrix):
    return np.linalg.inv(matrix)


def l_otwrot(matrix):
    kow = kowar(matrix)
    otwrot = macierz_odwrot(kow)
    return np.dot(otwrot, matrix.T)


def regresja_liniowa(matrix):
    x = np.array([[1, x[0]] for x in matrix])
    y = np.array([x[1] for x in matrix])
    lewa= l_otwrot(x)
    return np.dot(lewa, y)


test = np.array([[2, 1], [5, 2], [7, 3], [8, 3]])
print(regresja_liniowa(test))


# X * Beta = Y
# Beta = Y / X

# Beta = X^-1 * Y

# leewastronna odwrotność
# Beta = (X'transponowane' * X)^-1 * X'transponowane' * Y
# beta0 = 2/7
# beat1 = 5/14
# ostani wykłąd godz 22 min