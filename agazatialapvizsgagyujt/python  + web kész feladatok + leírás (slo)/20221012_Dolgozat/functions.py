from os import rename
from data import varosok

def varosokSzama():
    return len(varosok)

def tobbMint10M():
    darab = 0
    for varos in varosok:
        splitted = varos.split(';')
        if int(splitted[2]) > 10000000:
            darab += 1
    return darab

def legnepesebb():
    maxIndex = 0
    maxErtek = 0
    for i in range(1, len(varosok)):
        splitted = varosok[i].split(';')
        if int(splitted[2]) > maxErtek:
            maxIndex = i
            maxErtek = int(splitted[2])
    return maxIndex

def kinaiDarab():
    darab = 0
    for varos in varosok:
        splitted = varos.split(';')
        if splitted[1] == 'Kína':
            darab += 1
    return darab

def kinaiOsszes():
    osszeg = 0
    for varos in varosok:
        splitted = varos.split(';')
        if splitted[1] == 'Kína':
            osszeg += int(splitted[2])
    return osszeg

def orszagKeres(keresett):
    for varos in varosok:
        splitted = varos.split(';')
        if splitted[1] == keresett:
            return True
    return False