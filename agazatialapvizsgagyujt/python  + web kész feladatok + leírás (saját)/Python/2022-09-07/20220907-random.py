#dobjunk 20szor dobókockával

from random import randint

dobasok= []

for i in range(19):
    dobasok.append(randint(1 , 6))
print (dobasok)

for i in range (5):
    print(dobasok[i])

print('Másik megoldás:')
for egyDobas in dobasok[0:5]:
    print(egyDobas)

print('egymás alá írjuk ki az elemeket az 6. és a 12. között')
for i in range (5,12):
    print(f'{i+1}.:{dobasok[i]}')
   
print('Másik megoldás:')
for egyDobas in dobasok[5:12]:
    print(egyDobas)

    print('Egymás alá írjuk ki az utolsó 8 dobás eredményét')
    for i in range(11,19):
      print(f'{i+1}.:{dobasok[i]}')

print('Másik megoldás:')
for egyDobas in dobasok[11:19]:
    print(egyDobas)

    print('Harmadik megoldás:')
for egyDobas in dobasok[-8:]:#-8: hátulról visszafele megy az utolsó 8 darab
    print(egyDobas)