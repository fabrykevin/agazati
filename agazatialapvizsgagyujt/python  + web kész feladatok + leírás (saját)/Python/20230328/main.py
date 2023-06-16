from kaja import Kaja

Kajak:list[Kaja]=[]

file=open('teletal.csv', 'r', encoding='utf-8')

file.readline()

for row in file:
    Kajak.append(Kaja(row.strip()))

file.close()

print(f'2. feladat:A menüben {len(Kajak)} kaja szerepel')

db=0
for item in Kajak:
    if item.fajta=='Főétel':
        db+=1
print(f'3.feladat: A menüben {db } főétel szerepel')

legolcsobb=Kajak[0]

for item in Kajak:
    if item.ar<legolcsobb.ar:
        legolcsobb=item

print(f'4. feladat: A legolcsobb étel {legolcsobb.nev}')


legolcsobbM=None
for item in Kajak:
    if item.fajta=='Menü':
        if legolcsobbM==None or item.ar>legolcsobbM.ar:
            legolcsobbM=item

print(f'4.b feladat: A legolcsobb menü{legolcsobbM.nev}')


print('\n5.feladat\n')
csapat = ""
for item in eredmenyek:
    if "Barcelona" in item.hazai:
        csapat = item.hazai
    elif "Barcelona" in item.idegen:
        csapat = item.idegen
print(csapat)




legolcsobbMNev=''
legolcsobbMAr=99999999
for item in Kajak:
    if item.fajta=='Menü' and item.ar<legolcsobbMAr:
        legolcsobbMNev=item.nev
        legolcsobbMAr=item.ar

print(f'4. b2 feladat: Legolcsobb menü:{legolcsobbMNev}')

bevetelForint=0
for item in Kajak:
    if item.fajta=='Főétel':
        bevetelForint+=item.ar*item.mennyiseg

print(f'5.feladat:Árbevétel {bevetelForint*402.5} euro ')



stat={}
for item in Kajak:
    if item.fajta not in stat:
        stat[item.fajta] = item.mennyiseg
    else:
        stat[item.fajta] += item.mennyiseg
for key,value in stat.items():
    print(f"{key}.{value} db")



stat={}
for item in Kajak:
    if item.fajta in stat.keys():
        stat[item.fajta]+=item.mennyiseg
    else:
        stat[item.fajta]=item.mennyiseg


print(f'6.feladat: Statisztika')
for key, value in stat.items():
    print(f'\t{key} - {value} db')

arbevetel=int(input('7.feladat: Minimum árbevétel(Euro):'))
for item in Kajak:
    if item.arBevetelEuroban()< arbevetel:
        print(f'\t{item.nev}')
