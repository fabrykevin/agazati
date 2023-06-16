from __future__ import absolute_import


def menu():
    print('1. Abszolút érték számítás')
    print('2. Százalék számítás')
    print('3. Háromszög szerkeszthetőség')

    valasz= input('Mit szeretne csinálni (1-3)?:')
    if(valasz == '1'):
        a=int(input('Kérek egy számot: '))

        a = absolute(a)
        print(f'A szám abszolút értáke:{a}')
    elif(valasz =='2'):
        pass
    else:
        pass
    menu()