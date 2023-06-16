commandWord = input('Kérem a robot parancsait: ')
Ecount = 0
Ncount = 0
Dcount = 0
Kcount = 0
for letter in commandWord:
    if letter == 'E': 
        Ecount += 1
    elif letter == 'N': 
        Ncount += 1 
    elif letter == 'D': 
        Dcount += 1
    elif letter == 'K': 
        Kcount += 1
print(f'E betűk száma:{Ecount}')
print(f'N betűk száma:{Ncount}')
print(f'D betűk száma:{Dcount}')
print(f'K betűk száma:{Kcount}')




