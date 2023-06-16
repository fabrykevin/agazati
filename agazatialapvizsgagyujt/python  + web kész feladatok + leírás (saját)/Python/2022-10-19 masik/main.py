'''
1 van e ilyen nevű város a listában
2 hány város van az xy megyében
3 legkisebb lakosú város adatai
4 legnagyobb területű város adatai
5 átlag terület
6 irsz kereső név alapján

'''

from fuggvenyek import  varoskereso
from fuggvenyek import megye
from fuggvenyek import*

varos = input('add meg a varos nevet : ')

if varoskereso(varos) == False:
    print('nincs ilyen')
else : 
    print('van ilyen')

megyek = input('add meg a megye nevet : ')

print(f'a {megyek} nevű megyebe {megye(megyek)} db város van')

print(f'{legkisebbLakosuVaros()} es {lgkLakos(legkisebbLakosuVaros())}')

print(f'{legnagyobb()} km2 , {maxNev(legnagyobb())}  ')


print(f'{terulet()} km2 az atlag')

nev = input('add meg a nevet : ')
print(f' az {nev} nevű város irsz-je : {irsz(nev)}')