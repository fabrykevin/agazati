from adat import adatok

OsszesAdat:list[adatok] =[]
file=open('fob2016.txt', 'r', encoding='utf-8')
for row in file:
    OsszesAdat.append(adatok(row.strip()))

file.close()

print(f'3.feladat: Versenyzők száma:{len(OsszesAdat)}')
    
countWomen=0
for item in OsszesAdat:
    if item.kategoria=='Noi':
        countWomen+=1
print(f'4.feladat {countWomen/ len(OsszesAdat)*100:.2f}%')

winnerWoman=''
winnerWomanPoints=-1
for item in OsszesAdat:
    if item.totalPoints()>winnerWomanPoints:
        winnerWomanPoints=item.totalPoints()
        winnerWoman=item

print('6.feladat: A bajnok női versenyző')
print(f'\tNév:{winnerWoman.nev}')
print(f'\tEgyesület: {winnerWoman.egyesulet}')
print(f'\tÖsszpont: {winnerWoman.totalPoints()}')

file=open('osszpontFF.txt', 'w', encoding='utf-8')
for item in OsszesAdat:
    if item.kategoria=='Felnott ferfi':
        file.write(f'{item.nev}; {item.totalPoints()}\n')
file.close()

#dictionary nélkül

clubs=[]
for item in OsszesAdat:
    if item.egyesulet not in clubs:
        clubs.append(item.egyesulet)

for club in clubs:
    playerInClub=0
    for p in OsszesAdat:
        if p.egyesulet==club:
            playerInClub+=1
    if playerInClub>2 and club!='n.a':
        print(f'\t{club}-{playerInClub}fő ')


#dictionary
stats={}
for item in OsszesAdat:
    if item.egyesulet in stats.keys():
        stats[item.egyesulet]+=1
    else:
        stats[item.egyesulet]=1

for key,value in stats.items():
    if value>2 and key !='n.a':
        print(f'\t{key}-{value}fő ')
