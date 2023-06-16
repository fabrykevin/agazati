#- Készítse el az "Excel-es" HA függvényt.
#- paraméterek: feltétel, érték ha igaz, érték ha hamis

# operatorok <, >, <=, >=, =, <>
def keres(muvelet, muveletijel ):
    for index, item in enumerate(muvelet):
       if item == muveletijel:
        return index
    return False

def ha(feltetel, ertekIgaz,ertekHamis ):
    if '<=' in feltetel:
        index=keres(feltetel, '<')
        x=int(feltetel[0:index])
        y=int(feltetel[index+2:])
        if x<=y:
            return ertekIgaz
        else:
            return ertekHamis
    elif '>=' in feltetel:
        index=keres(feltetel, '>')
        x=int(feltetel[0:index])
        y=int(feltetel[index+2:])
        if x!=y:
            return ertekIgaz
        else:
            return ertekHamis
    elif '<>' in feltetel:
        index=keres(feltetel, '<')
        x=int(feltetel[0:index])
        y=int(feltetel[index+2:])
        if x!=y:
            return ertekIgaz
        else:
            return ertekHamis
    elif '=' in feltetel:
        index=keres(feltetel, '=')
        x=int(feltetel[0:index])
        y=int(feltetel[index+1:])
        if x==y:
            return ertekIgaz
        else:
            return ertekHamis
    elif '>' in feltetel:
        index=keres(feltetel, '>')
        x=int(feltetel[0:index])
        y=int(feltetel[index+1:])
        if x>y:
            return ertekIgaz
        else:
            return ertekHamis
    elif '<' in feltetel:
        index=keres(feltetel, '<')
        x=int(feltetel[0:index])
        y=int(feltetel[index+1:])
        print(x,y)
        if x<y:
            return ertekIgaz
        else:
            return ertekHamis
keplet=''
while keplet!='vége':
    keplet=input('Adja meg a képletet')
    if  keplet!='vége':
        ertekIgaz=input('Aja meg az igaz értéket')
        ertekHamis=input('Adja meg a hamis értéket')
        print(ha(keplet, ertekIgaz, ertekHamis))
