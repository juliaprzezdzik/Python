import keyword
keyword.kwlist #wypisywanie listy slow kluczowych
print('Hello')
#w pythonie funkcja main "fizycznie" nie istenieje
#print jest funkcja wbudowana (nie trzeba zalaczac biblioteki)
#None - obiekt pusty (zapisujemy z duzej litery)
#pass - pusta instrukcja (poniewaz kazdy blok musi zawierac konkretna instrukcje)
import builtins 
dir(builtins) #listowanie funkcji wbudowanych i wyjatkow 
import math
dir(math)
help(math.modf) #pobranie informacji z poziomu interpretera - w tym przypadku wyswietlenie dokumentacji funkcji modf(), zamykamy za pomoca q
dir(' ') #wyswietla liste funkcji dla lancuchow
help("".strip) #funkcja strip usuwa biale znaki
"".strip.__doc__ #dokumentacja metody strip
type('') #wyswietlanie informacji o typie obiektu (string)
type(" ")
a = 7 #dynamiczne typowanie
print(a)
print(type(a))
a = 1.5
print(type(a))
a = 1,1 #krotka - struktura danych przechowujaca sekwencje elementow
#po umieszczeniu zawartosci w krotce, nie mozna jej zmieniac
print(a)
print(type(a))
a = 1, "ania"
print(a)
a, b = 1, '2'
print(a, b)
a, *b = 1, '2', 3.,4,5
print(type(a), type(b)) #b to lista
print(a)
print(b)
#gwiazdki w pythonie uzywa sie np do funkcji ze zmienna iloscia paramedmntrow
print(1/2) #float
print(1//2) #int
print(1.//1.) #float bo wykonujemy dzialanie na dwoch liczbach zmiennoprzecinkowych
print(1./2) #float
print(1.//2) #1. to liczba zmiennoprzecinkowa; 1.0 dzielimy jak int, wynik: 0.0
#potegowanie:
print(2**3)
print(pow(2,3))
print(math.pow(2,3)) #float
print(pow(2,3,4)) #2 do potegi 3 modulo 4

print(math.ceil(1/3))
print(math.floor(1/3))
print(round(1/3))
print(round(1/3,3)) #zaokraglenie do 3 cyfr po przecinku
print(math.modf(1/3)) #wypisuje (czesc ulamkowa, czesc calkowita liczby)
print(math.modf(2.5))
print(min(2,11,3,4,2), max(2,11,3,4,2))
#a = -1,7
#print(abs(a), math.fabs(a)) 
#nie zadziala, bo te funkcje nie obsluguja krotek
a = -1
print(abs(a), math.fabs(a))
#abs to funkcja wbudowana - nie trzeba importowac modulu
#abs dla inta zwraca inta, dla floata - floata
#fabs zawsze zwraca floata

#instrukcje warunkowe:
#if warunek1:
#   instrukcja1(np. pass)
#elif warunek2:
#   instrukcja2
#else
#   instrukcja3

#bloki kodu tworzymy wcieciami (spacja/tabulator), ale nie mozna mieszac obu metod

#program umozliwiajacy rozwiazanie rownania kwadratowego

from math import sqrt #z modulu math importujemy sqrt
from cmath import sqrt as csqrt #importujemy funkcje dla liczb zespolonych i zmieniamy jej nazwe (aby nie pomylic z poprzednia)
a = float(input('a = ? '))
b = float(input('b = ? '))
c = float(input('c = ? '))
d = b**2-4*a*c
if d > 1e-6:
    x1 = (-b-sqrt(d))/(2*a)
    x2 = (-b+sqrt(d))/2/a
    print{f'x1={x1:.3f}, x2={x2:.3f}')
#f oznacza ze jest to f string
#:.3f oznacza zaokraglenie do trzech miejsc po przecinku
elif abs(d) <= 1e-6:
    x = -b/(2*a)
    print(f'x={x}')
else
    x1 = (-b-csqrt(d))/(2a)
    x2 = (-b+csqrt(d))/2/a
    print(f'x1={x1:.3f}, x2={x2:.3f}')

import sys #importowanie modulu umozliwiajacego korzystanie z argumentow wiersza polecen
import math
import cmath

if len(sys.argv)!=5 #sprawdzamy, czy dlugosc tablicy z argumentami ma dokladnie 5 elementow (pierwszy elemebt to nazwa progamu)
    sys.exit
a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])
eps = float(sys.argv[4])
if(d:=b**2-4*a*c)>eps:
    x1=(-b-math.sqrt(d))/(2*a)
    x2=(-b+math.sqrt(d))/(2*a)
    print(f'{x1=:.3f}, {x2=:.3f}')
elif math.fabs(d)<=eps:
    print(f'x1=x2={-b/(2*a):.2f}')
else:
    x1=(-b-cmath.sqrt(d))/(2*a)
    x2=(-b+cmath.sqrt(d))/(2*a)
    print(f'{x1=:.3f}, {x2=:.3f}')
print(d)

#krotki:
k = ()
print(type(k))
k = (1)
print(type(K)) #int 
k = (1,)
print(type(k)) #zeby utworzyc krotke jednoelementowa, nalezy dodac przecinek
print(k[0])
k = (1,2.3,'3', (4,7), [2,3,4])
print(len(k)) #wypisanie ilosci elementow krotki
# (4,7) to krotka w krotce
print(k[0], k[len(k)-1], k[-1])
#indeks ujemny oznacza obliczanie indeksow od konca
#k[-1] = 'a' nie mozemy tak zrobic bo krotki sa niemodyfikowalne
k[-1][1] = 'a' #tak mozna bo to nie jest krotka
print(k[-1])

#listy:
k = []
print(type(k))
k = [2]
print(type(k))
k = [2,]
print(type(k))
k = [1,2.3, '3', (4,7), [2,3,4], 4 ]
#listy sa modyfikowalne, ale jej niemodyfikowalne elementy (np.krotka) nie sa

bool(0), bool(1) #False, True
#sprawdzanie, czy np. lista, string zawieraja jakies elementy
bool([]), bool([1]) #False, True
bool(''), bool('a') #False, True
#pusty obiekt ma wartosc logiczna falszu, cala reszta - prawdy

#wycinki list
k = [8,0,17,1,10,13,19,13,10,3]
print(k[:]) #utworzenie kopii elementow listy
print(k[2:-3]) #wycinek listy od 2 elementu do 3 od konca
print(k[2:-3:2]) #skok co drugi element
print(k[2:]) #od drugiego elementu do konca
print(k[:-3])
print(k[::-1]) #wypisanie listy od konca
