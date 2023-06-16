from adat import helsinki

adatok: list[helsinki]=[]
file=open('helsinki.txt', 'r', encoding='utf-8')
for row in file: 
    adatok.append(helsinki(row.strip()))

file.close()

print(f'3.feladat:{len(adatok)} ')

print(f'')


statisztika={}
for item in adatok:
     if item.helyezes in statisztika.keys():
         statisztika[item.helyezes]+=1
     else:
         statisztika[item.helyezes]=1

print(f'Arany-{statisztika[1]}')
print(f'Ezüst-{statisztika[2]}')
print(f'Bronz-{statisztika[3]}')
print(f'Összesen-{statisztika[1]+ statisztika[2]+statisztika[1]}')
arany=0
ezust=0
bronz=0
for item in adatok:
    if item.helyezes==1:
        arany += 1
    elif item.helyezes==2:
        ezust+=1
    elif item.helyezes==3:
        bronz+=1

print(f' 4.feladat: \n{arany} \n{ezust}\n{bronz} \nÖsszesen:{arany+ezust+bronz}' )


pont=0
for item in adatok:
    if item.helyezes==1:
        pont+=7
    elif item.helyezes==2:
        pont+=5
    elif item.helyezes==3:
        pont+=4
    elif item.helyezes==4:
        pont+=3
    elif item.helyezes==5:
        pont+=2
    elif item.helyezes==6:
        pont+=1

print(f'5.feladat: {pont}')

# totalpoint=0
# for item in adatok:
#     totalpoint+=item.olympicPoints
#     print(f'5.feladat:\n{totalpoint}')

uszas=0
torna=0
for item in adatok:
    if item.helyezes<=3 and item.sportag=='torna':
        torna+=1
    elif item.helyezes<=3 and item.sportag=='úszás':
        uszas+=1
print('6.feladat: ')
if (uszas<torna):
    print('Torna sportágban szereztek több érmet.')
elif(torna<uszas):
    print('Torna sportágban szereztek több érmet.')
else:
    print('Egyenlő volt az érmek száma')
file=open('helsinki2.txt' , 'w',encoding='utf-8' )
for item in adatok:
    if item.helyezes==1:
            olympicPoints=7
    elif item.helyezes==2:
            olympicPoints=5
    elif item.helyezes==3:
            olympicPoints=4
    elif item.helyezes==4:
            olympicPoints=3
    elif item.helyezes==5:
            olympicPoints=2
    elif item.helyezes==6:
            olympicPoints=1
    if item.sportag=='kajakkenu':
        file.write(f'{item.helyezes} {item.sportolokSzama} {item.olympicPoints} {item.sportag} kajak-kenu {item.versenyszam}\n ')
    else:
        file.write(f'{item.helyezes} {item.sportolokSzama}{item.olympicPoints} {item.sportag} {item.versenyszam}\n ')

file.close()

maxValue=adatok[0].sportolokSzama
maxItem=adatok[0]
for item in adatok:
     if item.sportolokSzama>maxValue:
          maxValue=item.sportolokSzama
          maxItem=item
print('8.feladat:')
print(f'Helyezés: {item.helyezes}')
print(f'Sportág: {item.sportag}')
print(f'Versenyszám: {item.versenyszam}')
print(f'Sportolók száma: {item.sportolokSzama}')