from Épület import Épület
epuletek:list[Épület]=[]
file=open('Legmagasabb.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    epuletek.append(Épület(row.strip()))
file.close()
print(f'3.2 feladat:Épületek száma: {len(epuletek)} darab')

emeletosszeg=0
for item in epuletek:
    emeletosszeg+=item.emelet
print(f'3.3 feladat Emeletek összeg: {emeletosszeg}')


#londoni épületek emleteinek összege
emeletosszeg=0
for item in epuletek:
    if  item.város=='London':
        emeletosszeg+=item.emelet
print(f'3.3.1 feladat:Londoni épületek Emeletek összeg: {emeletosszeg}')

legmagasabb=epuletek[0]

for item in epuletek:
    if item.magasság>legmagasabb.magasság:
        legmagasabb=item
print(f'3.4 feladat A legmagasabb épület adatai:')
print(f'\tNév:{legmagasabb.név}')
print(f'\tVáros:{legmagasabb.város}')
print(f'\tOrszág:{legmagasabb.ország}')
print(f'\tMagasség:{legmagasabb.magasság}')
print(f'\tEmeletek száma:{legmagasabb.emelet}')
print(f'\tÉpítés éve:{legmagasabb.épület}')

for item in epuletek:
    if item.ország=='Olaszország':
        print('3.5 feladat: Van olasz épület az adatok között')
        break
else:
    print('3.5 feladat: Nincs olasz épület az adatok között')

#3.6 Hány épület van az egyes országpkban
stat={}

for item  in epuletek :
    if item.ország in stat.keys():
        stat[item.ország]+=1
    else:
        stat[item.ország]=1
print('3.6 feladat: Országonkénti statisztika')
for key, value in stat.items():
    print(f'\t{key} : {value} db')
