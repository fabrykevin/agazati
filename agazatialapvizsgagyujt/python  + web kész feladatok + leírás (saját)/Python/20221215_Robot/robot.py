commandWord=input('Kérem a robot parancsait:  ')
Kcount=0
Dcount=0
Ncount=0
Ecount=0
for letter in commandWord:
    if letter=='E':
        Ecount+=1
    elif letter=='N':
        Ncount+=1
    elif letter=='D':
        Ncount+=1
    elif letter=='K':
        Ncount+=1
print(f'E betűk száma:{Ecount}')
print(f'E betűk száma:{Ncount}')
print(f'E betűk száma:{Dcount}')
print(f'E betűk száma:{Kcount}')




