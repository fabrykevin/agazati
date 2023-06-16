from CBadás import CBadás

adasok : list[CBadás] = []

file = open('cb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    adasok.append(CBadás(row.strip()))
file.close()

print('3. feladat: CB-rádió')
print(f'3.2 feladat: Bejegyzések száma: {len(adasok)} db')

sanyiDb = 0
for item in adasok:
    if item.nev == 'Sanyi':
        sanyiDb += 1
print(f'3.3 feladat: sanyihoz tartozó bejegyzések száma: {sanyiDb} db')

legtobb = adasok[0]
for item in adasok:
    if item.adasDb > legtobb.adasDb:
        legtobb = item

for item in adasok:
    if item.adasDb == legtobb.adasDb:
        print(f'\tIdő: {item.ora}:{item.perc} Darab: {item.adasDb} Név: {item.nev}')

file = open('cb2.txt','w',encoding='utf-8')
file.write('Kezdes;Nev;AdasDb\n')
for item in adasok:
    file.write(f'{item.kezdes};{item.nev};{item.adasDb}\n')
file.close()

# Ki hány adást indított összesen?
stat = {}
for item in adasok:
    if item.nev in stat.keys():
        stat[item.nev] += item.adasDb
    else:
        stat[item.nev] = item.adasDb

print('+1 feladat: Statisztika')
for key,value in stat.items():
    print(f'\t{key}: {value}')
