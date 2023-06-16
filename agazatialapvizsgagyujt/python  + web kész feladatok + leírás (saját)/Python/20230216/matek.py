#Készítsen függvényt, ami elvégzi a paraméterben kapott egyszerű matematikai műveletet (+ - / *)
#    - pl.: "3 * 4" vagy "3*4" => 12
def keres(muvelet, muveletijel ):
    for index, item in enumerate(muvelet):
       if item == muveletijel:
        return index
    return False



def muveletek(muvelet):
    eredmeny=0
    muvelet=muvelet.replace(' ', '')

    muveletijelhelye=keres(muvelet, '+')
    if muveletijelhelye != False:

        x=float(muvelet[0:muveletijelhelye])
        y=float(muvelet[muveletijelhelye+1:])
        eredmeny=x+y
        return eredmeny
    muveletijelhelye=keres(muvelet, '-')
    if muveletijelhelye != False:
        
        x=float(muvelet[0:muveletijelhelye])
        y=float(muvelet[muveletijelhelye+1:])
        eredmeny=x-y
        return eredmeny
    muveletijelhelye=keres(muvelet, '*')
    if muveletijelhelye != False:
        
        x=float(muvelet[0:muveletijelhelye])
        y=float(muvelet[muveletijelhelye+1:])
        eredmeny=x*y
        return eredmeny
    muveletijelhelye=keres(muvelet, '/')
    if muveletijelhelye != False:
        
        x=float(muvelet[0:muveletijelhelye])
        y=float(muvelet[muveletijelhelye+1:])
        eredmeny=x/y
        return eredmeny

muvelet=input('Mit számoljunk ki?')
print(f'{muvelet} = {muveletek(muvelet)}')
