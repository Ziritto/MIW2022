import random as rand

def x(x):
    return x

def y(x):
    return x**2/2

def prostokaty(x, y, fx, lx, eps):
    rzeczywist = y(lx) - y(fx)
    wynik = 0
    dzielnik = 1
    while (abs(wynik - rzeczywist) > eps):
        wynik = 0
        dzielnik *= 2
        odleglosc = float(lx - fx) / float(dzielnik)
        for i in range(dzielnik):
            wynik += x(fx + odleglosc * i) * odleglosc
        print("ile prostokątów - {0}. wynik - {1}. Rzeczywiste: {2}.dzielnik - {3}.".format(wynik, rzeczywist, eps, dzielnik))
    return wynik


print(prostokaty(x, y, 0, 1, 0.05))



def montecarlo(x, y, fx, lx, dokladnosc):
    rzeczywist = y(lx) - y(fx)
    wynik = 0
    punkty = 1000
    minimum, maximum = x(fx), x(lx)
    losowanie = []
    ile = 0
    while (abs(wynik - rzeczywist) > dokladnosc):
        punkty += 1000
        for i in range(1000):
            newx = rand.uniform(fx, lx)
            newy = rand.uniform(minimum, maximum)
            while ((newx, newy) in losowanie):
                newx = rand.uniform(fx, lx)
                newy = rand.uniform(minimum, maximum)
            losowanie.append((newx, newy))
            wynik = x(newx)
            if (newy <= wynik):
                ile += 1
        wynik = (lx - fx) * (maximum - minimum) * (ile / punkty)
        print("ile punktów - {0}. wynik - {1}. Rzeczywiste: {2}. Dokłądność - {3}.".format(punkty,wynik,rzeczywist,dokladnosc))
    return wynik

print(montecarlo(x,y, 0, 1, 0.05))



