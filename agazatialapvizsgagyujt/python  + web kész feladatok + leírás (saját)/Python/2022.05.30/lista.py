import string


üresLista=[]
print(üresLista)
listaKezdőérték=[4,6,1,8,9]
print(listaKezdőérték)
gyümölcslista=["alma", "körte", "eper"]
   #egy elem elérése az index segítségével
  # az indexelés 0-tól kezdődik, elemszám 1 az utolsó elem index!!!
print(gyümölcslista[0])
  #print(stringLista[3])#IndexError:list index out of range


for item in listaKezdőérték:
    print(item)
    print(f'A gyümölcsök száma:{len(gyümölcslista)}')# a lista méretének (elemszámának) lekérdezése: len()
     
for index in range(0, len(gyümölcslista)):
    print(f'{index}. elem:{gyümölcslista[index]}')


újgyümölcs =input('Kérek egy gyümölcsöt:')
gyümölcslista.append(újgyümölcs)    #új elem hozzáadása a lista végéhez:listaneve.appened(újelem)
gyümölcslista.remove('alma')     #meglévő elem első előfordulásának eltávolítása a listából:listaneve.remove(elem)
  #gyümölcslista.remove('dinnye')#ha nincs az elem a listában:ValueError: list.remove(x): x not in list

listaKezdőérték.sort() #rendezés
print(listaKezdőérték)

print(gyümölcslista)
szam=int(input('Kérek egy számot, megmondom benne van e a listában:'))
if szam in listaKezdőérték: #in operátor: annak ellenőrzése, hogy egy érték benne van-e a listában
    print('Benne van')
else:
    print('Nincs benne')


#lista egy elemének módosítása
gyümölcslista[0]="narancs"




