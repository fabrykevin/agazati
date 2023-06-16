#kérjen be egy számot
#kérje be a számrendszert(2-9)
#írja ki a számot ebben a számrendszerben
#kérjen be egy másik számot a meggadott számrendszerben
#döntse-el hogy ez a szám megfelel-e számrendszerek
#ha, igen, akkor írja ki 10-es számrendszerben

from fuggvenyek import convertFrom10

szam=int(input("Kérjek egy számot:"))

szamrendszer=int(input("Kérem a számrendzert(2-9):"))

x=convertFrom10(szam, szamrendszer)
print(x)