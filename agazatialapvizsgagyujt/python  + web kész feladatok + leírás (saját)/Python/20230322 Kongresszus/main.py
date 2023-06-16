from adatok import adat
from math import floor
eloadasok:list[adat]=[]


file=open('eloadasok.txt', 'r', encoding='utf-8')
for row in file:
    eloadasok.append(adat(row.strip()))

file.close()


print(len(eloadasok))

daysStat={}

for item in eloadasok:
    if item.nap in daysStat.keys():
        daysStat[item.nap] +=1
    else:
        daysStat[item.nap]=1


#print(daysStat)
#eloadasok.sort()
for day in sorted(daysStat.keys()):
    print(f'November{day}.:')
    for item in eloadasok:
        if item.nap==day:
            print(f'\t{item.szam}. {item.nev}: {item.cim}')


timeStats={}
for item in eloadasok:
    if item.nap in timeStats.keys():
        timeStats[item.nap]+=item.hossza
    else: timeStats[item.nap]=item.hossza

print('Előadások hossza naponta ')
for key,value in timeStats.items():
    print(f'november{key}.: {floor(value/60)}:{value%60} perc')


max=0
maxPres=''
for item in eloadasok:
     if item.nap==6 and item.hossza>max:
        max=item.hossza
        maxPres=item
        print(f'{maxPres.nev}  ')

# #kérje be egy előadó nevét döntse el tart e előadást ah igen számolja meg hogy hányat

db=0
nev=input('Kérem az előadó nevét: ')
for item in eloadasok:
    if nev==item.nev:
        db+=1
        
if db==0:
    print('Nincs ilyen')
else:
    print(f'{db} db előadása van') 



counter=0
for item in eloadasok:
    if 'mikrofon'==item.eszkozok:
        db+=1
print(f'Az előadáson {counter} db eszköz kell')