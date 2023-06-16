
varosok=[]

f= open('varosok.csv', 'r', encoding='utf8')
elsoSor = f.readline()
for row in f:
   varosok.append(row.strip())
f.close()

print(varosok)

#print('szöveg' .strip(),   'vége', 'valami')
print(f'A városok száma:{len(varosok)}')


#ujVaros='Miskolc;Magyarország;211123\n'
#f=open('varosok.csv', 'a', encoding='utf8')
#f.write(ujVaros)
#f.close()

#hozzon létre egy orszagok.csv nevű fájlt, benne az összes országgal
#minden ország csak egyszer szerepeljen

f=open('orszagok.csv', 'w' , encoding='utf8')
#x- írásra nyitja meg a fájlt, ami benne van azt kitörli
for sor in varosok:
    adatok=sor.split(';')
    f.write(adatok[1]+'\n')
f.close()


orszagok=[]
for sor in varosok:
    adatok=sor.split(';')
    if adatok[1] not in orszagok:
        orszagok.append(adatok[1]) 
orszagok.sort()
print(orszagok)

f= open('orszagok.csv', 'w' , encoding='utf8')
for orszag in orszagok:
    f.write(orszag  +'\n')
f.close()

 #f= open('orszagok.csv', 'w' , encoding='utf8')
#f.writelines(orszagok)
#f.close()