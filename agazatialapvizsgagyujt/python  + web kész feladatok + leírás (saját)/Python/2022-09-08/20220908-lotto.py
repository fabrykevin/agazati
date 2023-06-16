#lottó szám sorsolás
#5/90 , 6/45, 7/35

import random


lottoSzamok = []

def sorsolas(darab, osszes):
    while  len(lottoSzamok) < darab:
        kihuzottSzam = random.randint(1, osszes )
        if kihuzottSzam not in lottoSzamok:
            lottoSzamok.append( kihuzottSzam )



#sorsolas(5, 90)
sorsolas(7, 45)
print(lottoSzamok)