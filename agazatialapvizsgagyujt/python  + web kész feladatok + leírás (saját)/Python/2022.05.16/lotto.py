from random import randint


def lotto(szamDb,tartomany):
    for i in range(1,szamDb+1):
        szam = randint(1, tartomany)
        print(szam, end=' ')
        print()

print('szerencejáték Zrt')
print('Kérem válasszon (1-3)')
print('1-Ötöslottó')
print('2-Hatoslottó')
print('3-Skandináv lottó')
típus=input('Kérem válasszon (1-3):')
if típus=='1':
    print('Ötöslotó nyerőszámok')
    lotto(5,90)
elif típus=='2':
    print('Hatoslottó nyerőszámok')
    lotto(6,45)
elif típus=='3':
    print('Skandináv lottó nyerőszámok')
    lotto(7,35)
else:
    print('Nincs ilyen opció!')
    
