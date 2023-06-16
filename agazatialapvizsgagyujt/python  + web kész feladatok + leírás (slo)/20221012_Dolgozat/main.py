from functions import *
from data import varosok

print('5. feladat: Legnépesebb város:')
legnepesebbVarosIndexe = legnepesebb()
splitted = varosok[legnepesebbVarosIndexe].split(';')
print(f'\tNeve: {splitted[0]}')
print(f'\tOrszág: {splitted[1]}')
print(f'\tLakosság: {splitted[2]}')

print(f'6. feladat: A {kinaiDarab()} legnagyobb kínai város összlakossága: {kinaiOsszes()}')

orszag = input('7. feladat: Kérem az ország nevét: ')
if orszagKeres(orszag) == True:
    print(f'{orszag}i város szerepel a listában.')
else:
    print(f'{orszag}i város NEM szerepel a listában.')
