# x = input('podaj imie - ')
# print ('czesc ,'+x)

#3 zmienne 1 string, 2 liczba całkowita, 3 zmiennoprzecinkowa, wypisz format

a = "test"
b = 10
c = 10.5

wynik = "zmienna 1 - {0}, zmienna 2 - {1}, zmienna 3 - {2}".format(a,b,c)
print(wynik)
print()

# zmienna lista, w liście kilka słów złączyć za pomocą #

lista = ["jeden","dwa","trzy","cztery","pięć"]
hasz = "#".join(lista)
print(hasz)
print()

# rodziel to teraz

split = hasz.split("#")
print(split)
print()

# ciąg znaków

# zopisz ile było znaków
zmienna = "MedotyInżynieriiWiedzySąNajlepsze"
wynik2 = "Długość znaków w zmiennej - {0}, długość - {1}" .format(zmienna, len(zmienna))
print (wynik2)
print()

test1 = zmienna.lower()
print(test1)
print()

usuwanie = zmienna.replace("ż"," ").replace("ą"," ").replace(" ","")
wynik3 =  "Długość znaków w zmiennej - {0}, długość - {1}" .format(usuwanie, len(usuwanie))
print(wynik3)
print()

aaaa = set(usuwanie)
wynik4 =  "wartość - {0}, długość - {1}" .format(aaaa, len(aaaa))
print(wynik4)
print()

# tabu !!!
a1 = "aaaaaa"
a2 = 10


lista2 = ['python','c++','c#','java','PHP']
print(len(lista2))
test3 = lista2.index('c++')
print(test3)
print()
# extend rozszesz zmienną , + robi nową
print(lista+lista2)
test6 = lista + lista2
print(len(test6))
print()
print()
# apend - dodawanie, insert
#słownik

słownik = {
    "alkochol" : "wódka",
    "procent" : "40",
}

kraje = {
    "kraj" : ["Rosja","Litwa","Białoruś","Ukraina","Słowacja","Czechy","Niemcy"],
    "stolica" : ["Moskwa","Wilno","Mińsk","Kijów","Bratusława","Praga","Berlin"]
}

print(kraje['stolica'])

#Jak przesortować słownik!!!!!!!!!!!

print(bool( ))
print(bool(" "))
print(bool("0"))
print(bool(0))
print(bool([" "," "]))
print()
print()

# zdanie czy ma więcej niż 15 unikalnych znaków. (set)
zdanie = "Filip jest bardzo powolny za zajęciach"
sprawdzanie = set(zdanie)
dlugosc = len(sprawdzanie)

if dlugosc > 15:
    print("ma więcej unikalnych elementów niż 15")
else:
    print("ma mniej unikalnych elementów niż 15")
print()

for i in range(1, 11):
    print(i)
print()

for i in hasz:
    if i == "#":
        i = " "
    print(i)

print('------------------------------------')
#------------------------------------ tydzień 2

# złącz to w szystko w jeden
#haslo = input('podaj podaj haslo - ')
#print (haslo)
#haslo_dlugosc = len(haslo)

# if haslo_dlugosc > 10:
 #   if i == '!'
 #   if not 'A' <= i and i <= 'Z':


#for i in haslo:
#    if 'A' > i and i < 'Z':
#        print('brak duzych liter')
#        break
#    if not i == '!':
#        print('brak ! w hasłu')
#        break



#czy należy jeden return i 1 while

#test21 = 'aaaaaaWMaaaaaaa'


# while zamiast for. licznik od 0
# flaga == flase
# i = 0
# while i < len(lista);
#    if l[i++] == e;
#    flaga = True;
#    break

#flaga2 == False
#licznik = 0
#while i < len(test21):
#    if test21[licznik] == 'U':
#        flaga = True
#        print('tak')
#        break
#

# tworzymy plik. w pliiku wpisz 3 linijki medoty inży wiedzy. plik otwórz i wypisz zawartosć print
# ( )
# ( ,end='')

plik = open("plik2.txt", "a")
plik.write("Metody ")
plik.write("Inżynierii ")
plik.write("wiedzy ")
plik.close()

# with open("plik2.txt", "e") as file:
#   for i line in file
#       print()

# lista z stringów zapisz do pliku. Uzyj print
#
#lista22 = ['python','c++','c#','java','PHP']
#plik2 = open("plik3.txt")
#while i in lista22:
#    plik2.write(lista22.index(i))
#plik2.close()

#------------------------- dobrze
#plik3 = open("plik3.txt","x")
#plik3.write("Metody\n")
#plik3.write("Inzynierii\n")
#plik3.write("Wiedzy\n")
#plik3.close()

file4 = open('plik3.txt', 'r')
print(file4.read())
file4.close()
#-------------------------
# lista z 4 miastami, tworzymi listę z pierwszymi 3 literami miast. funkcja map(). i wypisać to lambda()

miasta = ['olsztyn','białystok','warszawa','kraków']
a = list(map(lambda w: w[:3],miasta))
print(a)

# mamy liste. w liście nazwy plików. stwórz funkcję która zwraca nazwy plikow z konkternym rozrzeszeniem. podajemy parametr

# kolenje zadanie to samo jako generator ?

lista_plikow = ['txt.txt','py.py','html.html','css.css']

# def x(lista, ext)
#    wynik=[]
#   for e in lista:
#       if e.endwith(ext):
#           wynik.append(e)
#   return wynik


# def x(lista, ext)

#   for e in lista:
#       if e.endwith(ext):
#           yield e
