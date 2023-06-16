from random import randint, randrange

dobas=randint(1,6)
dobás=randint(1,6)
while dobas !=6 or dobás !=6:
    print(f'{dobas},{dobás}')
    dobas =randint(1,6)
    dobás =randint(1,6)
print('Mindkét kockával 6-ost dobtál, VÉGE.')


