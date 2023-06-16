from math import radians
from kocka import felszin
from menu import felszinVagyTerfogat, foMenu
from kup import*

valasz = foMenu()
if valasz == 'A':
    print('Téglatest felszín/térfogat számítás')
     aOldal = (int(input('A oldal:'))
     bOldal = (int(input('B oldal:'))
     cOLdal = (int(input('C oldal:'))
     if felszinVagyTerfogat() == 'A':
          print(f'A téglalap feslszíne={Teglalap}')
          
elif valasz == 'B':
     Boldal= int(input('B oldal:'))
     if felszinVagyTerfogat()=='B':
     print('Gömb felszín/térfogat számítás')
     radius=(int(input('radius: '))
     if felszinVagyTerfogat() == 'A':
          print(f'A gömb felszíne={gömbfelszin(sugar)}')
     else: 
          print(f'A gömb térfogata={gömbterfogat(sugar)}')

elif valasz == 'C':
     print('Gúla felszín/térfogat számítás')
     int(input('magasság'))
elif valasz == 'D':
     print('Kúp felszín/térfogat számítás')
     sugar =()
elif valasz == 'E':
     print('Kocka felszín/térfogat számítás')
     aOldal = int(input('A oldal:'))
     if felszinVagyTerfogat() == 'A':
        print(f'A kocka felszíne = {Kockafelszin(aOldal)}')
     else:
          print(f'A kocka térfogata = {terfogat(aOldal)}')
