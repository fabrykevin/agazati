from CBadás import CBadás

adasok: list[CBadás]=[]

file=open('cb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    adasok.append(CBadás(row.strip()))

file.close()
print('3.feladat: CB-Rádió')
print(f'3.2 feladat: Bejegyzések száma:{len(adasok)} db')

sanyidb=0
for item in adasok:
    if item.nev=='Sanyi':
        sanyidb+=1

print(f'3.3 feladat:sanyihoz tartozó Bejegyzések száma:{sanyidb} db')


legtobb=adasok[0]

for item in adasok:
    if item.adasDB>legtobb.adasDB:
        legtobb=item

for item in adasok:
    if item.adasDB==legtobb.adasDB:
        print(f'\t{item.ora}:{item.perc} darab:{item.adasDB} Név:{item.nev}')


file=open('cb2.txt', 'w', encoding='utf-8')

file.write('Kezdes;Nev;AdasDB\n')
for item in adasok:
    file.write(f'{item.kezdes};{item.nev};{item.adasDB}\n')


file.close()


statisztika={}
for item  in adasok :
    if item.nev in statisztika.keys():
        statisztika[item.nev]+=item.adasDB
    else:
        statisztika[item.nev]=item.adasDB

for key, value in statisztika.items():
    print(f'\t{key} : {value} db')
