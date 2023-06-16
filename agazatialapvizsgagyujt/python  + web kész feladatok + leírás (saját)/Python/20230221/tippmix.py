#2 feladat
#-Készítsen függvényt paraméterek:
#   - paraméter 1: odds (pl.: 1.25)
#   - paraméter 2: tét
#   - visszatérés-> várható maximális nyeremény
#-Készítsen másik függvényt, melyik eldönti, hogy nyert-e
#   - paraméter 1: odds(pl.: 1.25)
#   - visszatérés :logikai

import random

def maxNyeremeny(odds, osszeg):
    return osszeg*odds
    
def jatek(odds):#1:6
    x=odds.split(':')
    osszeseset=int(x[1])
    joesetekszam=int(x[0])
    veletlen=random.randint(1,osszeseset)
    return veletlen<= joesetekszam





