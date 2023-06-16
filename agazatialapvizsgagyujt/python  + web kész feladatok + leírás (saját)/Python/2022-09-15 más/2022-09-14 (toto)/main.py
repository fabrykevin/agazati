import math
import random

def ujTipp(n):
    tipp = ''
    while tipp != '1' and tipp !='2' and tipp != 'X':
        if n == 14:
            tipp = input(f'Az Ön tippje a 13+1-es mérkőzésre: ').upper()    
        else:
            tipp = input(f'Az Ön tippje a {n}. mérkőzésre: ').upper()
    return tipp

def tippekBekerese():
    t = []
    for i in range(1, 15):
        t.append(ujTipp(i))
    return t

def eredmenyekGeneralasa():
    t = []
    for i in range(1, 15):
        cs1 = random.randint(0,5)
        cs2 = random.randint(0,5)
        t.append(cs1 * 10 + cs2)
    return t

def eredmeny2tipp(eredmeny):
    # 34 -> 2 , 41 -> 1, 33 -> x
    cs1 = math.floor(eredmeny / 10)
    cs2 = eredmeny % 10
    if cs1 > cs2:
        return '1'
    elif cs2 > cs1:
        return '2'
    else:
        return 'x'

tippek = tippekBekerese()
eredmenyek = eredmenyekGeneralasa()
helyesDarab = 0
for i in range(1, 15):
    helyes = tippek[i-1] == eredmeny2tipp(eredmenyek[i-1])
    if helyes:
        print(f'{i}. mérkőzés: játékos tippje: {tippek[i-1]}, eredmény: {math.floor(eredmenyek[i-1] / 10)}-{eredmenyek[i-1] % 10}, a tipp helyes')
        helyesDarab+=1
    else:
        print(f'{i}. mérkőzés: játékos tippje: {tippek[i-1]}, eredmény: {math.floor(eredmenyek[i-1] / 10)}-{eredmenyek[i-1] % 10}, a tipp nem helyes')
print('A helyes tippek száma', helyesDarab)