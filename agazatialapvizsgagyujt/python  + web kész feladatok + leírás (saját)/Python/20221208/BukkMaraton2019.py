from versenytav import Versenytav
from functions import *

Beolvas('bukkm2019.txt')
print(f'Versenytávot nem teljesítők{CelbaerkezokAranya():.3}%.')
print(f'Rövid távon idult nők száma: {Versenyzokszama("Rövid" ,"Nő")}')
print(f'Mini távon idult nők száma: {Versenyzokszama("Mini" ,"Férfi")}')
if VoltTobbMint(6*60*60):
    print('Volt olyan versenyző aki, több mint 6 órán át volt a pályán.')
else:
    print('Nem volt olyan versenyző aki, több mint 6 órán át volt a pályán.')

print(f'A felnőtt férfi kategórií győztese rövid távon:{Gyoztes("Rövid", "ff")}')
gyoztes=AbszolutGyoztes("Rövid", "ff")
print(f'\tRajtszám:{gyoztes.rajtszam}')
print(f'\tNév:{gyoztes.nev}')
print(f'\t Egyesület:{gyoztes.egyesulet}')
print(f'\tIdŐ:{gyoztes.ido}')

