atlag=[]
nev=input('Diák neve: ')
for i in range(5):
    tantargyneve=('Tantárgy neve:')
    x=int(input(f'{tantargyneve} jegyek'))

osszeg=0
def jegyertkeles(jegyek):
    for jegy in jegyek:
        atlag.append(jegy / 2)
osztalyzatok = []
for atlag in atlag:
    if atlag >= 4.5:
        osztalyzatok.append(5)
    elif atlag >= 3.5:
        osztalyzatok.append(4)
    elif atlag >= 2.5:
        osztalyzatok.append(3)
    else:
        osztalyzatok.append(2)
    

    
    evvegiatlag = sum(atlag) / len(atlag)
if evvegiatlag >= 4.5:
    osztondij = 100000
elif evvegiatlag >= 4.0:
    osztondij = 50000
elif evvegiatlag >= 3.5:
    osztondij = 30000
else:
    osztondij = 0

    
    
        

