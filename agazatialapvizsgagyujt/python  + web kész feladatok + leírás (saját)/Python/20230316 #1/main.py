from Ultrabalaton import adatok

UltraBalatonadatok:list[adatok]=[]
file=open('ub2017egyeni.txt ', 'r', encoding='utf-8')
file.readline()
for row in file:
    UltraBalatonadatok.append(adatok(row.strip()))

file.close()

print(f'3.feladat Egyéni indulók: {len(UltraBalatonadatok)} fő')

count=0
for item in UltraBalatonadatok:
    if item.Kategoria=='Noi' and item.TavSzazalek=='100':
        count+=1

print(f'4.feladat: Célba érkező női sportolók:{count} fő')

print('5.feladat:')
nev=input('Kérem a sportoló nevét: ')
for item in UltraBalatonadatok:
    if item.Versenyzo==nev and item.TavSzazalek=='100':
        print('Igen')
        print('Igen')
        break
    elif item.Versenyzo==nev and item.TavSzazalek!='100':
        print('Igen')
        print('Nem')
        break
    elif item.Versenyzo != nev:
        pass
else:
    print('Nem')
        

db=0
ido=0
for item in UltraBalatonadatok:
        if item.Kategoria=='Ferfi' and item.TavSzazalek=='100':
            db+=1
            ido +=item.ido()
print(f"7. feladat: Átlagos idő: {ido/db}")


print('8. feladat: ')

legjobbferfi=1000
ferfi=''
legjobbnoi=1000
noi=''
for item in UltraBalatonadatok:
    if item.Kategoria=='Ferfi' and item.TavSzazalek=='100'and item.ido()<legjobbferfi:
        legjobbferfi=item.ido()
        ferf=item
    if item.Kategoria=='Noi' and item.TavSzazalek=='100'and item.ido()<legjobbnoi:
        legjobbnoi=item.ido()
        noi=item
print(f'{item.}'))





        
    



