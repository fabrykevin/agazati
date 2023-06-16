import math


def gulafelszin(aOldal, magyasság):
    magyasságPalast = math.sqrt ( math.pow (aOldal 1/2)+math.pow(magyasság))
    palastTerulet=aOldal*magyasságPalast /2 

    return aOldal*aOldal+4*palastTerulet


def gulaterfogat(aOldal, magasság):
    
    return aOldal*aOldal*magasság/3
   