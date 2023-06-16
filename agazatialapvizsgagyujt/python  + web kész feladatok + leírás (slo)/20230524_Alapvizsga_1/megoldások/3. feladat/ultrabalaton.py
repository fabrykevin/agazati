from versenyzo import versenyzo

versenyzok : list[versenyzo] = []

file = open('ub2017egyeni.txt','r',encoding='utf-8')
file.readline()
for row in file:
    versenyzok.append(versenyzo(row))
file.close()

print(f'3.2 feladat: Futók száma: {len(versenyzok)}')

noi_darab = 0
for item in versenyzok:
    if item.kategoria == 'Noi' and item.szazalek == 100:
        noi_darab += 1
print(f'3.3 feladat: Célba érkező női sportolók: {noi_darab} fő')

leghosszabb_nevu = versenyzok[0]

for item in versenyzok:
    if len(item.nev) > len(leghosszabb_nevu.nev):
        leghosszabb_nevu = item
print('3.4 feladat: A leghosszabb nevű futó')
print(f'\tNév: {leghosszabb_nevu.nev}')
print(f'\tRajtszám: {leghosszabb_nevu.rajtszam}')
print(f'\tEredmény: {leghosszabb_nevu.ido}')

ferfi_ido_osszeg = 0
ferfi_darab = 0
for item in versenyzok:
    if item.kategoria == 'Ferfi' and item.szazalek == 100:
        ferfi_darab += 1
        ferfi_ido_osszeg += item.ido_oraban
print(f'3.5 feladat: Férfi sportolók átlagos ideje: {ferfi_ido_osszeg/ferfi_darab} óra')