import abc
from ast import Return
from itertools import count
from data import results

def countCompetitors():
    return len(results)
#maximumkiválasztás

def typeStringToNumber(type):
    #talaj-->4
    #lólengés-->5
    if type=='Talaj':
        return 4
    elif type =='Lólengés':
        return 5
    elif type =='Gyűrű':
        return 6
    elif type =='Nyújtó':
        return 7
    elif type =='Korlát':
        return 8
    elif type =='Ugrás':
        return 9
    return False






def winner(competitionType):
    typeNumber=typeStringToNumber(competitionType)
    maxPoint=0
    winnerName=''
    for result in results:
        resultList = result.split(';')
        point = float(resultList[typeNumber].replace(',','.'))
        if point> maxPoint:
            maxPoint=point
            winnerName=resultList[1]
    return winnerName
    
def ringResult(StartNumber):
    for result in results:
        resultList = result.split(';')
        if resultList[0]== StartNumber:
            return resultList[6]
    return False

def countlessTehnPommelHorse(limit):
    count=0
    for result in results:
        resultList = result.split(';')
        if limit> float(resultList[5].replace(',','.')):
            count+=1
    return count


def regions():
    regionsList=[]
    for result in results:
        resultList = result.split(';')
        if resultList[3] not in regionsList:
            regionsList.append (resultList[3])

    regionsList.sort()
    return regionsList



def countCompetitiorsOfCountries():
    countries=[]
    
    for result in results:
        resultList = result.split(';')
        if resultList[2] not in countries:
            countries.append (resultList[2])
    

    for country in countries:
        count=0
        for result in results:
            resultList = result.split(';')
            if resultList[2]== country:
                count+=1
        print(f'{country}:{count} fő')



