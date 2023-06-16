from fuggvenyek import lakossag
from varosok import városok
from fuggvenyek import *

print(f'A listában {varosokszama()} város szerepel')
print('Legalább 10 milliós városok száma')



print(lakosokszama())

print(f'Legnépesebb lakosú város{lakossag()}')



varos=input(f'Kérem az orszég nevét:{Legnepesebbvaros()}')

if varos==városok:
    print( 'Nincs ilyen város')
else:
    print('Van ilyen város')




