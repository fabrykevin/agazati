def foMenu():
    valasz = ''
    while valasz !='A' and valasz != 'B' and valasz != 'C' and valasz != 'D' and valasz !='E' and valasz !='X':
        print('X - Kilépés')
        print('A - téglatest')
        print('B - Gömb')
        print('C - Gúla')
        print('D - Kúp')
        print('E - Kocka')
        print('X - Kilépés')

        valasz = input('választás: ').upper()  
    return valasz

def felszinVagyTerfogat():
    valasz = ''
    while valasz !='A' and valasz != 'V':
        print('\nMit szeretne kiszámolni? ')
        print('\tA - Felszín')
        print('\tV - térfogat')
 
        valasz= input('Választás: ').upper()
    return valasz