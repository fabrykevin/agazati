#- Készítsen magyarországi mobilszám ellenőrző fv-t:
#	- Lehetséges mobil formátumok: "06 20 123-45 67", "+36 301234567", van más ??
#	- "körzetszámok": 20 30 70 50 31 ?


def mobilszamellenorzes(szam: str):
    szam = szam.replace(' ','')
    szam = szam.replace(' -','')
    if szam[0]=='+':
        szam = szam.replace('+ ','00')
    if szam[0:4] =='0036':
        szam=szam.replace('0036', '06')
    if szam[0:2] != '06':
        return False
    if szam[2:4] != '20'and szam[2:4] !='30' and szam[2:4] !='70' and szam[2:4] !='50':
        return False
    if len(szam) !=11:
        return False
    return True


szam= input('Adja meg a telefonszámot:')
if mobilszamellenorzes(szam) == True:
    print('A mobiltelefon szám  helyes')
else:
    print('A mobiltelefon szám helyes ')