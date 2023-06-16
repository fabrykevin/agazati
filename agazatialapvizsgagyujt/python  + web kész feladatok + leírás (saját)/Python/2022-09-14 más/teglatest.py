
def teglatestAdatok():
    a = float(input('"a" oldal hossza: '))
    b = float(input('"b" oldal hossza: '))
    c = float(input('"c" oldal hossza: '))

    return [a, b, c]

def teglatestFelszin():
    # l = teglatestAdatok()
    # a = l[0]
    # b = l[1]
    # c = l[2]
    a, b, c = teglatestAdatok()

    print(f'A téglatest felszíne: {2 * (a * b + b * c + c * a)}')

def teglatestTerfogat():
    a, b, c = teglatestAdatok()

    print(f'A téglatest térfogata: {a * b * c}')