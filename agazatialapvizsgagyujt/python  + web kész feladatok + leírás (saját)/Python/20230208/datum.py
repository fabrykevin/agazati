# Olvasson be egy dátumot és függvény(ek) segítségével döntse el, hogy a dátum helyes-e

def szokoev(ev):
    if ev % 4 != 0:
        return False
    if ev % 100 == 0 and ev % 400 != 0 :
        return False
    return True

def datumEll(datum):
    splittedData = datum.split('.')
    if len(splittedData) != 3:
        return False
    Ev = int(splittedData[0])
    Honap = int(splittedData[1])
    Nap = int(splittedData[2])
    honapok = [31,28,31,30,31,30,31,31,30,31,30,31]        
    if Honap > 12:
        return False
    if szokoev(Ev):
        if Honap == 2  and Nap > 30:
            return False
    elif Nap > honapok[Honap-1]:
        return False
    if Ev > 2023:
        return False
    return True

datum = input('Kérem a dátumot (ÉÉÉÉ.HH.NN):')


if datumEll(datum) == True:
     print('A dátum megfelelő')
else:
     print('A dátum nem megfelelő')
