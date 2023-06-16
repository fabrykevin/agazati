from Repulo import Repulo
import math

repulok : list[Repulo] = []
# repulok = []

file = open('utasszallitok.txt','r', encoding='utf-8')
elsosor = file.readline()
for row in file:
    repulok.append(Repulo(row.strip()))
file.close()

print(f'4. feladat: Adatsorok száma: {len(repulok)}')

boeing_darab = 0
for item in repulok:
    if 'Boeing' in item.tipus:
        boeing_darab += 1
print(f'5. feladat: Boeing típusok száma: {boeing_darab}')

max_utas_repulo = repulok[0]
for item in repulok:
    if item.utas_szam > max_utas_repulo.utas_szam:
        max_utas_repulo = item
print('6. feladat: A legtöbb utast szállító repülőgéptípus')
print(f'\tTípus: {max_utas_repulo.tipus}')
print(f'\tElső felszállás: {max_utas_repulo.ev}')
print(f'\tUtasok száma: {max_utas_repulo.utas}')
print(f'\tSzemélyzet: {max_utas_repulo.szemelyzet}')
print(f'\tUtazósebesség: {max_utas_repulo.utazosebesseg}')

file = open('utasszallitok_new.txt','w',encoding='utf-8')
file.write(elsosor)
# file.write('típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv\n')
for item in repulok:
    file.write(f'{item.tipus};{item.ev};{item.utas_szam};{item.szemelyzet_szam};{item.utazosebesseg};{round(item.felszallotomeg/1000)};{round(item.fesztav*3.2808)}\n')
file.close()


# Hány repülőt gyártottak az egyes években
stat = {}
for item in repulok:
    if item.ev in stat.keys():
        stat[item.ev] += 1
    else:
        stat[item.ev] = 1

print('Statisztika:')
for key,value in stat.items():
    print(f'{key}: {value} darab')



tolonyomas = float(input('Tolónyomás: '))
statikusnyomas = float(input('Statikus nyomás:'))
mach_szam = math.sqrt(5*(math.pow(tolonyomas/statikusnyomas+1,2/7)-1))
print(f'Mach-szám: {mach_szam}')