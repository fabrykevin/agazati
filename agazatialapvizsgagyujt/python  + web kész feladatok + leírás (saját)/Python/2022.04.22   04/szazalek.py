def atmentTanulokSzazaleka(összesTanuloDb, bukottTanuloDb):
    if összesTanuloDb > 0 and összesTanuloDb >= bukottTanuloDb:
        százalék = (1 - bukottTanuloDb/összesTanuloDb) * 100
    else:
        százalék=0
    return százalék 

print('Százalék számítás')
összes=int(input('Összes Tanulók száma:'))
bukott=int(input('Bukott tanulok száma:'))
százalék =atmentTanulokSzazaleka(összes, bukott)
if százalék==-1:
    print('Hibás adatok, ebből nem számolható százalék!')
else:
    print(f'A tanulók {százalék} %-a ment át a vizsgán.')
#     print('ez még az else-ben van.')
# print('ez már nem az else-ben van!!!')
