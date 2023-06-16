from data import varosok

def nagyvaros():
    count = 0
    for varos in varosok:
        darabolt = varos.split(';')
        if int(darabolt[2]) > 10000000:
            count += 1
    return count

def legnepesebb():
    legnagyobb = 0
    
  
    for varos in varosok:
        darabolt = varos.split(';')
        if int(darabolt[2]) > legnagyobb:
            legnagyobb = int(darabolt[2])
    return legnagyobb

def legnepesebbNev(legnagyobb):
    for varos in varosok:
        darabolt = varos.split(';')
        if int(darabolt[2]) == legnagyobb:
            return darabolt[0]

def legnepesebbOrszag(legnagyobb):
    for varos in varosok:
        darabolt = varos.split(';')
        if int(darabolt[2]) == legnagyobb:
            return darabolt[1]

    

def kinaiVarosok():
    osszeg = 0
    for varos in varosok:
        darabolt = varos.split(';')
        if darabolt[1] == 'Kína':
            osszeg += int(darabolt[2])
    return osszeg

def orszagKeres(orszag):
     for varos in varosok:
        darabolt = varos.split(';')
        if darabolt[1] == orszag:
            return True
     return False


