import math


def oraperc(ido):
    ora=math.floor(ido/60)
    perc=ido-ora*60
    #Írja meg a függvény többi részét!
    return str(ora) + ' óra' + str(perc) + ' perc'
   