def foMenu():
    print('\n\n1..Téglatest')
    print('2..Gömb')
    print('3..Gúla')
    print('4..Kúp')
    print('5..Henger')
    print('\n0..Kilépés a programból')

    v = ''
    while v != '0' and v != '1' and v != '2' and v != '3' and v != '4' and v != '5':
        v = input('\nVálasztás: ')

    return int(v)

def felszinVagyTerfogat():
    print('\n\nA..Felszín')
    print('V..Térfogat')
    print('X..Vissza')

    v = ''
    while v != 'A' and v != 'V' and v != 'X':
        #  v = input('\nVálasztás: ')
        #  v = v.upper()
        v = input('\nVálasztás: ').upper()
        
    return v
