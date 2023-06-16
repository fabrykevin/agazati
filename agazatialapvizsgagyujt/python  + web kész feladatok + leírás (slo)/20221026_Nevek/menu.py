def menu():
    option = -1
    while option < 0 or option > 5:
        print('0 - Kilépés')
        print('1 - Listázás')
        print('2 - Keresés')
        print('3 - Új')
        print('4 - Törlés')
        print('5 - Módosítás')
        option = int(input('Váasszon a fentiek közül: '))
    return option