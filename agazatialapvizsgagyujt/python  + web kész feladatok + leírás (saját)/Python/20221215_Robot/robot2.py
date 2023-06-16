
def countLetters(letter, word ):
    counter=0
    for charachter in word:
        if charachter==letter:
            counter+=1
    return counter

commandWord=input('Kérem a robot parancsait:  ')
Kcount=countLetters("K", commandWord)
Dcount=countLetters("D", commandWord)
Ncount=countLetters("N", commandWord)
Ecount=countLetters("E", commandWord)
print(f'E betűk száma:{Ecount}')
print(f'N betűk száma:{Ncount}')
print(f'D betűk száma:{Dcount}')
print(f'K betűk száma:{Kcount}')

if Ncount>Kcount:
    Ncount-=Kcount
    Kcount=0
else:
    Kcount-=Ncount
    Ncount=0

if Dcount>Ecount:
    Dcount-=Ecount
    Ecount=0
else:
    Ecount-=Dcount
    Dcount=0

print(f'Wgy legrövidebb út parancsszava:{"E"*Ecount}{"N"*Ncount}{"K"*Kcount}{"D"*Dcount}')