#amig 0 nem lesz a szam
#KÉRJÜNK BE EGÉSZ SZÁMOT
szamok = []

#szamok.append(12)
#szamok.append(22)
#szamok.append(32)

#for i in range(5):

#   szam= int(input('Kérek egy számot:'))
#  szamok.append(szam)

szam = 1
while szam != 0 or len(szamok) == 0:

    szam = int(input('Kérek egy számot [0 - VÉGE]:'))
    if szam!= 0:
        szamok.append(szam)

print(szamok)
if len(szamok) !=0:
    osszeg = 0
    for egySzam in szamok:
        #camel case
        #sneke case
        #Pascal case
        #osszeg = osszeg + egySzam
        osszeg += egySzam
        print(f'A számok átlaga:{ osszeg / len (szamok)}')
        max = szamok [0]
        for egySzam in szamok:
            if egySzam >max:
                max= egySzam
        print(f'A legnagyobb szám:{max}')
else:
    print('Nincs egyetlen szám sem a listában, nem számolható átlag.')
