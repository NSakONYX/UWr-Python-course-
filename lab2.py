"""
Zadanie 1. 
(1p) Napisz procedurę szachownica(n,k), 
która rysuje kwadratową szachownicę, o boku 2*n, 
składającą się z kwadratów o boku k, jak na poniższym 
rysunku (na którym pokazany jest wynik wywołania szachownica(4,3) ).

   ###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
   ###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
###   ###   ###   ###
"""

def szachownica(n,k):
    if (n<1 or k<1): print("")

    counter = 0
    changer = 0


    for _ in range (2*k*n):
        counter += 1

        if (changer==1):

            if (counter % k == 0):
                changer = 0
            print(("*"*k + " "*k) * n)
        else: 

            if (counter % k == 0):
                changer = 1
            print((" "*k + "*"*k) * n)

szachownica(3,5)