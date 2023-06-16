from Pilota import Pilota

pilotak: list[Pilota] = []

file = open('pilotak.csv' , 'r', encoding='utf-8')
file.readline()
for item in file:
    pilotak.append(Pilota(item.strip()))

file.close()

print(f'3. feladat: {len(pilotak)}')
print(f'4. feladat: {pilotak[-1].nev}')
print('5. feladat:')
for item in pilotak:
    if item.ev < 1901:
        print(f'\t {item.nev} ({item.datum}) ')

min = 999999999
nemzetiseg = 0
for item in pilotak:
    if item.rajtszam != '':
        if int(item.rajtszam) < min: 
            min = int(item.rajtszam)
            nemzetiseg = item.nemzetiseg
print(f'6. feladat: {nemzetiseg}')


min = 999999999
minIndex = 0
for index,item in enumerate(pilotak):
    if item.rajtszam != '':
        if int(item.rajtszam) < min: 
            min = int(item.rajtszam)
            minIndex = index
print(f'6. feladat: {pilotak[minIndex].nemzetiseg} {pilotak[minIndex].nev}')

statisztika = {}
for item in pilotak:
    if item.rajtszam in statisztika.keys():
        statisztika[item.rajtszam] += 1
    else: 
        statisztika[item.rajtszam] = 1
    
x = []

for key,value in statisztika.items():
    if value >= 2 and key != '':
      x.append(key)
print(', '.join(x))

