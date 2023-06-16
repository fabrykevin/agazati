# Dobjunk dobókockával 30-szor,
# Írjuk ki az egyes dobások eredményét
# a végén egy statisztikát arról, hány db-est, 2-est...6-ost dobtunk
 
from ast import If
import random
from re import X

def kockadobas(sorszam):
    x=random.randint(1,6)
    print(f'{sorszam}.dobás:{X}')
    return x

egyes=0
kettes=0
hármas=0
négyes=0
ötös=0
hatos=0

for i in range(1,31):
    dobas= kockadobas(i)
    
    if   dobas==1:
        egyes+=1
    elif dobas==2:
        kettes+=1
    elif dobas==3:
        hármas+=1
    elif dobas==4:
        négyes+=1
    elif dobas==5:
        ötös+=1
    else:
        hatos+=1


print('\nStatisztika:')
print(f'\t1.esek:{egyes} db')
print(f'\t2.esek:{kettes} db')
print(f'\t3.esek:{hármas} db')
print(f'\t4.esek:{négyes} db')
print(f'\t5.esek:{ötös} db')
print(f'\t6.esek:{hatos} db')
