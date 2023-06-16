from helsinki1952 import helsinki

adatok:list[helsinki] = []

file = open('helsinki.txt', 'r', encoding='utf-8')
for row in file:
    adatok.append(helsinki(row.strip()))
file.close()

print(f'3.feladat: \nPontszerző helyezések száma: {len(adatok)} ')
print('4.feladat:')

statisztika = {}
for item in adatok:
    if item.place in statisztika.keys():
        statisztika[item.place] += 1
    else:
        statisztika[item.place] = 1

print(f'Arany - {statisztika[1]}')
print(f'Ezüst - {statisztika[2]}')
print(f'Bronz - {statisztika[3]}')
print(f'Összesen: {statisztika[1] + statisztika[2] + statisztika[3]}')

totalPoints = 0
for item in adatok:
    totalPoints += item.olympicPoints
print(f'5.feladat:\nOlimpiai ponok száma: {totalPoints}')

uszas = 0
torna = 0
for item in adatok:
    if item.place <= 3 and item.sport == 'torna':
        torna += 1
    elif item.place <= 3 and item.sport == 'uszas':
        uszas += 1

print('6. feladat:')
if uszas < torna:
    print('Torna sportágban szereztek több érmet.')
elif torna < uszas:
    print('Uszas sportágban szereztek több érmet.')
else:
    print('Egyenlő volt az érmek száma.')

file = open('helsinki2.txt','w', encoding='utf-8')
for item in adatok:

    if item.place == 1:
        olympicPoints = 7
    else:
        olympicPoints = 7 - item.place

    if item.sport == 'kajakkenu':
        file.write(f'{item.place} {item.numberOfMembers} {olympicPoints} kajak-kenu {item.category}\n')
    else:
        file.write(f'{item.place} {item.numberOfMembers} {olympicPoints} {item.sport} {item.category}\n')
file.close()

maxValue = adatok[0].numberOfMembers
maxItem = adatok[0]
for item in adatok:
    if item.numberOfMembers > maxValue:
        maxValue = item.numberOfMembers
        maxItem = item

print('8. feladat')
print(f'Helyezés: {maxItem.place}')
print(f'Sportág: {maxItem.category}')
print(f'Versenyszám: {maxItem.sport}')
print(f'Sportolók száma: {maxItem.numberOfMembers}')
