from jelolt import Jelolt

jeloltek:list[Jelolt] = []

def keres(nev):
    for item in jeloltek:
        if item.nev == nev:
            return item
    return False

file = open('szavazatok.txt', 'r', encoding='utf-8')
for item in file:
    jeloltek.append(Jelolt(item.strip()))

file.close()

print(f'2. feladat: A választáson {len(jeloltek)} képviselőjelölt indult.')

nev = input('Írja be a képviselőjelölt nevét: ')
talalat = keres(nev)
if talalat == False:
    print('Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!')
else:
    print(f'3. feladat: Képviselő neve: {talalat.nev} \n\tA jelölt a {talalat.kerulet}-s számú körzetben indult\n\tA kapott szavazatok száma: {talalat.szavazatokSzama}')

osszes = 0
for item in jeloltek:
    osszes += item.szavazatokSzama
print(f'4. feladat: A választáson {osszes} szavazó a jogosultak {(osszes / 12345) * 100}%-a vett részt.')

# max = jeloltek[0]
# for item in jeloltek:
#     if item.szavazatokSzama > max.szavazatokSzama:
#         max = item
# print(f'5. feladat: A legtöbb szavazat: {max.nev} - {max.part}: {max.szavazatokSzama} szavazat.')

maxErtek = 0
maxElem = ''
for item in jeloltek:
    if item.kerulet == 1 and item.szavazatokSzama > maxErtek:
        maxErtek = item.szavazatokSzama
        maxElem = item
if maxElem.part == '-':
    print(f'5+1. feladat: A legtöbb szavazat az első kerületben: {maxElem.nev} - független: {maxElem.szavazatokSzama} szavazat.')        
else:    
    print(f'5+1. feladat: A legtöbb szavazat az első kerületben: {maxElem.nev} - {maxElem.part}: {maxElem.szavazatokSzama} szavazat.')        

stat = {}
for item in jeloltek:
    if item.part in stat:
        stat[item.part] += item.szavazatokSzama
    else:
        stat[item.part] = item.szavazatokSzama
print('6. feladat')
for key, value in stat.items():
    if key == '-':
        print(f'\tFüggetlen: {value} szavazatok.')
    else:
        print(f'\t{key}: {value} szavazatok.')

file = open('TISZ.csv', 'w', encoding='utf-8')

file.write('Körzet;Név;Szavazatok száma\n')
for item in jeloltek:
    if item.part == 'TISZ':
        file.write(f'{item.kerulet};{item.nev};{item.szavazatokSzama}\n')

file.close()

