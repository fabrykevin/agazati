from Price import price
euro=307.7
prices:list[price]=[]

file=open('uzemanyag.txt', 'r', encoding='utf-8')
for row in file:
    prices.append(price(row.strip()))
file.close()

print(f'3.feladat:Változások száma: {len(prices)}')
minDiff=prices[0].difference
for item in prices:
    if item.difference<minDiff:
        minDiff=item.difference
print(f'4 feladat: A legkisebb különbség: {minDiff}')

countDiff=0
for item in prices:
    if item.difference==minDiff:
        countDiff+=1
print(f'3.feladat: A lekisebb különbség előfordulása:{countDiff}')

for item in prices:
    if item.leapDay==True:
        print('6.feladat: Volt változás szökőnapon')
        break
else:
    print('Volt változás szökőnapon')

file=open('euro.txt', 'w', encoding='utf-8')
for item in prices:
    file.write(f'{item.date}; {item.petrol/euro:.2f}; {item.diesel/euro:.2f}\n')

file.close 