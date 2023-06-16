from data import telepulesek

def telepulesekSzama():
    return len(telepulesek)

#összegzés
def osszesLakos():
    osszeg = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        osszeg += int(telepulesAdatok[4])
    return osszeg

#minumum kiválasztás
def legkisebb():
    #min = 9999999999
    #vagy szebben:
    elso = telepulesek[0].split(';')
    minMeret = int(elso[3])
    minNev = elso[0]

    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if minMeret > int(telepulesAdatok[3]):
            minMeret = int(telepulesAdatok[3])
            minNev = telepulesAdatok[0]

    return minNev

def nagykozsegek():
    darab = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if telepulesAdatok[1] == 'nagyközség':
            darab += 1
    return darab

def telepulesTersege(keresettTelepules):
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')
        if telepulesAdatok[0] == keresettTelepules:
            return telepulesAdatok[2]
    return False

def zahonyi1500():
    darab = 0
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')    
        if telepulesAdatok[2] == 'Záhonyi' and int(telepulesAdatok[3]) > 1500:
            darab += 1
    return darab 

def legtobbLakosuKozseg():
    maxLakos = 0
    maxNev = ''
    for telepules in telepulesek:
        telepulesAdatok = telepules.split(';')    
        if telepulesAdatok[1] == 'község' and int(telepulesAdatok[4]) > maxLakos:
            maxLakos = int(telepulesAdatok[4])
            maxNev = telepulesAdatok[0]
    return maxNev