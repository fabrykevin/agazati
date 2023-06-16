import math


def gombSugar():
    r = float(input('Sugár hossza: '))
    return r

def gombFelszin():
    r =  gombSugar()

    print(f'A gömb felszíne: {4 * math.pi * r *r}')

def gombTerfogat():
    r =  gombSugar()

    print(f'A gömb térfogata: {4/3 * math.pi * r * r * r}')

def valami():
    pass
