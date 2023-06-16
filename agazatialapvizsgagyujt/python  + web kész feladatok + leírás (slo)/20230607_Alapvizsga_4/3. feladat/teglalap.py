print('1. feladat: Téglalap területe és kerülete')
for i in range(10):
    print(f'Adja meg a(z) {i+1}. téglalap oldalait')
    try:
        # raise ValueError('Hiba')
        a = float(input('a = '))
        b = float(input('b = '))
        print(f'T = {a * b}')
        print(f'K = {(a + b) * 2}')
    except:
    # except ValueError as error:
        print('Nem megfelelő adat!')