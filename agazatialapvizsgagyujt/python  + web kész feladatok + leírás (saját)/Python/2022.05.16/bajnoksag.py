from random import randint


def randomEredmeny(maxGolokSzama):
    hazai=randint(0,maxGolokSzama)
    vendeg=randint(0,maxGolokSzama)
    print(f'{hazai} : {vendeg}')
    if hazai>vendeg:
        return 3
    elif hazai==vendeg:
        return 1
    return 0
print('a bajnokság eredményei')
pont=0
for i in range(1,16):
    pont +=   randomEredmeny(5)
print(f'Szerzett pontok száma összesen {pont} ')