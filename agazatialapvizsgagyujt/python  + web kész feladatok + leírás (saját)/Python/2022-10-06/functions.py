from ast import Return
from data import telepulesek

def telepulesekszama():
    return len(telepulesek)
#összegzés
def osszeslakos():
    osszeg=0
    for telepules in telepulesek:
        telepulesAdatok=telepules.split(';')
        osszeg+=int(telepulesAdatok[4])
    return osszeg
#minimum kiválasztás
def legkisebb():
    #min=9999999999
#vagy
    minMeret = 99999999
    for telepules in telepulesek:
         telepulesAdatok=telepules.split(';')
         if minMeret> int(telepulesAdatok[3]):
            minMeret=int(telepulesAdatok[3])
    return telepulesAdatok[0]

def nagykozsegek():
    darab=0
    for telepules in telepulesek:
         telepulesAdatok=telepules.split(';')
         if telepulesAdatok[1]=='nagyközség':
            darab+=1
    return darab

def telepulesTersege(település):
    for telepules in telepulesek:
        telepulesAdatok=telepules.split(';')
        if telepulesAdatok[0] == település:
            return telepulesAdatok[2]
    return False

def hektar():
    terulet=0
    for telepules in telepulesek:
         telepulesAdatok=telepules.split(';')
         if telepulesAdatok[2]=='Záhonyi' and int(telepulesAdatok[3]) >=1500:
            terulet+=1
    return terulet





def legnagyobbKozseg():
    maxlakos=0
    maxNev=''
    for telepules in telepulesek:
         telepulesAdatok=telepules.split(';')
         if telepulesAdatok[2]=='község' and int(telepulesAdatok[3]) >maxlakos:
            maxlakos    =int(telepulesAdatok[4])
            maxNev=telepulesAdatok[0]
    return maxNev