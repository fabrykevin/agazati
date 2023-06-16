from data import varosok
from fuggvenyek import nagyvaros
from fuggvenyek import legnepesebb
from fuggvenyek import kinaiVarosok
from fuggvenyek import orszagKeres
from fuggvenyek import legnepesebbNev
from fuggvenyek import legnepesebbOrszag

print(f'A listában {len(varosok)} város szerepel')

print(f'Legalább 10 milliós városok száma: {nagyvaros()}')

print(f'Legnépesebb város: \n \t Neve : {legnepesebbNev(legnepesebb())} \n \t Orszag: {legnepesebbOrszag(legnepesebb())} \n \t Lakosság: {legnepesebb()}')

print(f'a 17 legnagyobb kínai város összlakossága: {kinaiVarosok()}')

orszag = input('Kérem az ország nevét:')

if orszagKeres(orszag) == False:
    print(f'{orszag}i város nincs a listában')
else:
    print('van ilyen')