from random import randint
from this import d


def dobas():
    d1=randint(0,20)
    if randint(1,25)==25:
        d1=25
    if d1 !=25 and randint(1,10)==10:
        d1*=3
    elif randint(1,5)==5:
        d1*=2
    return d1
allas=301
while allas >0:
        d=dobas()
        if allas-d>=0:
            allas-=d
        else:
            print('Besokallt')
        print(f'Állás:{allas}')

    