"""
zadanie 1. pomijamy. zadanie tematyczne/wstępne.
"""


"""
Zadanie 2. Jak wiadomo n! = 1 · 2 · · · · · n. Napisz w pythonie definicję funkcji silnia. Napisz program, który wypisuje następujący raport:

4! ma 2 cyfry
5! ma 3 cyfry
6! ma 3 cyfry
7! ma 4 cyfry
8! ma 5 cyfr
...

Raport powinien kończyć się na liczbie 100. Przy liczeniu liczby cyfr możesz skorzystać z następujących funkcji 
(nie opisujemy ich działania, jedynie podajemy przykładowe wywołania. Spróbuj, znając je i wpisując w interpreterze, 
domyśleć się tego działania, większość zresztą była omawiana na wykładzie):

str(123)
str(123)+str(123)
int(3.141592)
len("ala ma kota")
log(10)
log(2.7182818284590451)
log(1000)/log(10)

Funkcja log musi być zaimportowana z modułu math. Liczbę cyfr można liczyć na dwa sposoby. 
Wybierz jeden, a prowadzącemu opowiedz o drugim. 
Uwaga: napisy powinny być poprawne gramatycznie (czyli musisz użyć właściwej formy słowa cyfra). Jeżeli tego nie zrobisz, za zadanie dostaniesz 0.8p.


"""

print("\n\n\nZadanie 2\n")

#funkcja pomocnicza
"""
Inne metody to przy użyciu (len(str(int))) lub przy użyciu log() do czego trzeba zaimportować moduł math
"""
def intLength(integer):
    length = 1

    while (integer != 0): 
        integer //= 10
        length += 1 

    return length

def silnia(liczba):
    a = 1
    for i in range (1, liczba+1):
        a = a*i
    if (intLength(a)<5): print(liczba,"! ma ",intLength(a)," cyfry") 
    else: print(liczba,"! ma ",intLength(a)," cyfr")

#program
for i in range(1, 101):
    silnia(i)

print("\n\n\nZadanie 3\n")
"""
Zadanie 3. (0.5p) Napisz procedurę krzyzyk(n), która rysuje krzyżyk z gwiazdek, 
składający się z 5-ciu kwadratów o boku n, jak na poniższym rysunku (na którym 
pokazany jest wynik wywołania krzyzyk(4) ). „Rysowanie” jest oczywiście wykonywane
za pomocą wywołań funkcji print.

    ****
    ****
    ****
    ****
************
************
************
************
    ****
    ****
    ****
    ****

"""

def cross(size):
    for _ in range (size):
        print(size*" "+size*"*"+size*" ")

    for _ in range (size):
        print(3*size*"*")

    for _ in range (size):
        print(size*" "+size*"*"+size*" ")

cross(6)


"""
Zadanie 4. Hasła losowane są dość bezpieczne, niemniej trudno się je zapamiętuje. 
Twoim zadaniem będzie napisać funkcję, która losuje łatwe do zapamiętania hasło 
(które zarazem pozostaje dość bezpieczne). Takie hasło będzie się składać z losowych 
krótkich fragmentów tekstu, tak dobranych, że łatwo się je wymawia po połączeniu. 
Funkcja losująca te fragmenty znajduje się w module losowanie_fagmentow, który powinieneś 
pobrać ze strony wykładu, umieścić w kartotece, w której znajduje się Twój program. Wówczas program:

from losowanie_fagmentow import losuj_fragment
for i in range(5):
    print (losuj_fragment())

może wypisać coś w stylu:

sia
je
tra
kawa
ce

(wiemy, że istnieją fragmenty o długości 2,3 oraz 4, natomiast nie ma żadnych innych) 
Musisz napisać funkcję losuj_haslo(n), która losuje hasło, składające się ze wspomnianych fragmentów, o długości 
dokładnie n znaków. Zademonstruj działanie tej funkcji pisząc program, który wywołuje ją 10 razy
 dla n=8 oraz 10 razy dla n=12 i wypisuje wyniki. Uwaga: każdy fragment powinien mieć możliwość zostania wylosowanym
"""

from losowanie_fragmentow import losuj_fragment

