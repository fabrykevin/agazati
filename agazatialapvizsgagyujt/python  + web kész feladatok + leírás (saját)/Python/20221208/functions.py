from versenytav import Versenytav

versenytavok=[]
def Beolvas(fajlnev):
    file=open(fajlnev , 'r', encoding='utf8')
    file.readline()
    for sor in file:
        vt=Versenytav(sor)
        #print(vt.nev)
        versenytavok.append(vt)

    file.close()

def CelbaerkezokAranya() -> float:
    return (1-len(versenytavok)/691)*100
#megszámlálás
def Versenyzokszama(tav, nem):
    darab=0
    for vt in versenytavok:
        if vt.Tav()==tav: 
            if vt.Nem()==nem:
                darab+=1
    return darab
#eldöntés
def VoltTobbMint(masodperc) -> bool:
    for vt in versenytavok:
        if vt.masodpercek>masodperc:
                return True
    return False

#minimumkiválasztás
def AbszolutGyoztes() -> Versenytav:
    min=versenytavok[0]
    for vt in versenytavok:
        if vt.masodpercek<min.masodpercek:
            min=vt
    return min
def Gyoztes(tav, kategoria):
    min=99999999999
    gyoztesversenyzo=''
    for vt in versenytavok:
         if tav==vt.tav and kategoria==vt.kategoria and vt.masodpercek<min:
            min=vt.masodpercek
            gyoztesversenyzo=vt
    return gyoztesversenyzo




    



