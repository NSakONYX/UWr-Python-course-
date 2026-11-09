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

print("\n\n\nZadanie 1")

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

print("\n\n\nZadanie 2")
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