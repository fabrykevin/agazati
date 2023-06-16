from data import lista


def varoskereso(varos):
    for elem in lista:
        darabolt = elem.split(';')
        if darabolt[0] == varos:
            return True
    return False
        
        
def megye(megyek):
    count = 0
    for elem in lista:
            darabolt = elem.split(';')
            if darabolt[2] == megyek:
                count += 1
    return count

def legkisebbLakosuVaros():
    minimum = 99999999999999
    for elem in lista:
        darabolt = elem.split(';')
        if  int(darabolt[5]) < minimum:
            minimum = int(darabolt[5])
    return minimum
        
def lgkLakos(minimum):
     for elem in lista:
        darabolt = elem.split(';')
        if int(darabolt[5]) == minimum:
           return darabolt[0:5]
        
def legnagyobb():
    maximum = 0
    for elem in lista:
        darabolt = elem.split(';')
        if float(darabolt[6].replace(',', '.')) > maximum:
            maximum = float(darabolt[6].replace(',', '.'))
    return float(maximum)
def maxNev(maximum):
     for elem in lista:
            darabolt = elem.split(';')
            if float(darabolt[6].replace(',', '.')) == maximum:
                return darabolt[0]
            
def terulet():
    ossz = 0
    for elem in lista:
        darabolt = elem.split(';')
        ossz += float(darabolt[6].replace(',', '.'))
    return ossz/len(lista)

def irsz(nev):
     for elem in lista:
        darabolt = elem.split(';')
        if darabolt[0] == nev:
            return darabolt[7]