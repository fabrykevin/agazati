from re import S
from functions import *
from functions import telepulesekszama

print(f'Települések száma Szabolcs-Szatmár-Bereg megyében{telepulesekszama()}')
print (f'A megye lakosság: {osszeslakos()} fő')

print(f'A legkisebb település: {legkisebb()}')

print(f'A megyében: {nagykozsegek()} darab nagyközség található')

telepules=input('Település neve: ')
terseg=telepulesTersege(telepules)
if terseg==False: 
    print(f'Nincs ilyen nevű település')
else:
    print(f'A {telepules} a {terseg} térségben található')


print(f'A záhonyi térségben {hektar()} db van')
print(f'MAX {legnagyobbKozseg}')