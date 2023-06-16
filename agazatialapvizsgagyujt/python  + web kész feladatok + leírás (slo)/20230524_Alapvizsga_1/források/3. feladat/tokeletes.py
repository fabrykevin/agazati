def tokeletes_e(szam):
    osszeg = 0
    for i in range(1,szam):
        if szam % i == 0:
            osszeg += i
    if osszeg == szam:
        return True
    return False

print('2. feladat: Tökéletes számok')
print('Kérek két természetes számot')
tól = int(input('tól = '))
ig = int(input('ig = '))

tokeletes_lista = []

for i in range(tól, ig+1):
    if tokeletes_e(i):
        tokeletes_lista.append(i)

print(f'Tökéeletes számok {tól} és {ig} között:')

if len(tokeletes_lista) == 0:
    print('A megadott tartományaban nincsen tökéletes szám.')
else:
    print(*tokeletes_lista, sep='; ')
