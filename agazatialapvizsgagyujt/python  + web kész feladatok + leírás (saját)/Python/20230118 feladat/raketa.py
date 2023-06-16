visszaszamlalas=int(input('Hány órás visszaszámlálást tervezünk?'))
felfuggesztesekszam=0
for i in range(visszaszamlalas, 0, -1):
    print(f'visszaszamlalas:{i}')
    felfuggesztes=input('Fel kell függeszteni a visszaszámlálást (i/n)?')
    if felfuggesztes =='i':
        felfuggesztesekszam+=1
print(f'A rakéta a visszaszámlálást követően ennyi órával indult:{visszaszamlalas+felfuggesztesekszam} ')