

def vizsgaeredemeny(szam):
    if szam>=48:
        return True
    else:
        return False
nev='a'
while nev !='':
    nev=input('Add meg a vizsgázó nevét!' )
    if nev!='':
        szam=float(input('Add meg a pontszámát!' )) 
        if vizsgaeredemeny(szam)==True:
            print(f'{nev} vizsgája sikeres.')
        else:
            print(f'{nev} vizsgája sikertelen.')

        