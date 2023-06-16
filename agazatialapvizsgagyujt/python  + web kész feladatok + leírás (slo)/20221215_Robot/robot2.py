def countLetters(letter, word):
    counter = 0
    for character in word:
        if character == letter:
            counter += 1
    return counter

commandWord = input('Kérem a robot parancsait: ')
Ecount = countLetters("E", commandWord)
Ncount = countLetters("N", commandWord)
Dcount = countLetters("D", commandWord)
Kcount = countLetters("K", commandWord)
print(f'E betűk száma:{Ecount}')
print(f'N betűk száma:{Ncount}')
print(f'D betűk száma:{Dcount}')
print(f'K betűk száma:{Kcount}')

if Ncount > Kcount:
    Ncount -= Kcount
    Kcount = 0
else:
    Kcount -= Ncount
    Ncount = 0

if Dcount > Ecount:
    Dcount -= Ecount
    Ecount = 0
else:
    Ecount -= Dcount
    Dcount = 0

print (f'Egy legrövidebb út parancsszava:{"E"*Ecount}{"N"*Ncount}{"K"*Kcount}{"D"*Dcount}')
