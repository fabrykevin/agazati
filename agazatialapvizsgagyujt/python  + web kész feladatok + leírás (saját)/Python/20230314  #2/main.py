from animal import Animal
Animals : list[Animal]=[]
file=open('Animals.csv' , 'r', encoding='utf-8')
file.readline()
for row in file:
    Animals.append(Animal(row.strip()))

file.close()

print(f'A listában {len((Animals))} db állat található')
city=input('Kérek egy várost: ')
print('Állatok ebben a városban:')
for item in Animals:
    if item.city == city:
        print(f'\t {item.name}, ({item.species})')
month=0
# month=input(int('Kérem a hónapot: '))
while month>12 or month<1:
    month=int(input('Kérem a hónapot: '))
day= int(input('Kérem a napot: '))
print('Ezen a napon születtek')


#varos, nev (faj):20 eves
for item in Animals:
    if month==item.month and day==item.day:
        if item.year==0:
            print(f'{item.city} : {item.name}({item.species}) Kora ismeretlen')
        else:
            print(f'{item.city} : {item.name}({item.species}) : {2023-item.year} éves')


count=0
for item in Animals:
    if item.born=='':
        count+=1
print(f'{count} db állatnak nem tudjuk az életkorát')

stat={}

for item in Animals:
    if item.species in stat.keys():
        stat[item.species]+=1
    else:
        stat[item.species]=1


print('5.feladat statisztika')
for key,value in stat.items():
    print(f'\t {key}:{value}db')    


file2=open('ogre.txt', 'w', encoding='utf-8')
for item in Animals:
    if item.species=='Ogre':
        file2.write(f'{item.city}; {item.name};{item.born}  \n')

file2.close()