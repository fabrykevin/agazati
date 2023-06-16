import math


def prim(szam):
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True
print('Prímszám vizsgálata')
szam= int(input("Kérek egy számot:"))
if prim(szam):
    print('A megadott szám prím')
else:
    print('A megadott szám nem prím')
