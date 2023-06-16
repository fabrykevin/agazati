# Százalék számítás (hányan mennek át az alapvizsgán)

def atmentTanulokSzazaleka(osszesTanuloDb, bukottTanuloDb):
    if osszesTanuloDb > 0 and osszesTanuloDb >= bukottTanuloDb:
        szazalek = (1 - bukottTanuloDb / osszesTanuloDb) * 100
    else:
        szazalek = -1
    return szazalek


print('Százalék számítás')
# szazalek = atmentTanulokSzazaleka(15,3)
osszes = int(input('Összes tanuló száma: '))
bukott = int(input('Bukott tanulók száma: '))
szazalek = atmentTanulokSzazaleka(osszes, bukott)
if szazalek == -1:
    print('Hibás adatok, ebből nem számolható százalék!')
else:    
    print(f'A tanulók {szazalek} %-a ment át a vizsgán.')
    # print('Ez még az else-ben van.')
# print('Ez már nem az else-ben van!!!')