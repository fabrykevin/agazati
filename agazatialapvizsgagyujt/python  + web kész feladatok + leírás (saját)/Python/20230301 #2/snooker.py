from snookeradatok import adat
versenyzok:list[adat]=[]
file=open('snooker.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    versenyzok.append(adat(row.strip()))


file.close()

print(f'3.feladat: A világranglistán  {len(versenyzok)} versenyző szerepel.')


ossz=0
for item in versenyzok:
    ossz+=item.Nyeremeny
print(f'4.feladat: A versenyzők átlagosan {ossz/len(versenyzok)} fontot kerestek.')

max=0
mmaxIndex=0
for index,item in enumerate(versenyzok):
     if item.Orszag =='Kína':
         if int(item.Nyeremeny)>max:
             max=int(item.Nyeremeny)
             maxIndex=index





print(f'5 feladat: A legjobban kereső kínai versenyző:\n\tHelyezés:{versenyzok[maxIndex].helyezes}\n\tNév: {versenyzok[maxIndex].Nev}\n\tOrszág: {versenyzok[maxIndex].Orszag}\n\tNyeremény összege:  {versenyzok[maxIndex].Nyeremeny*380} ')


for item in versenyzok:
    if item.Orszag=='Norvégia':
        print(f"6.feladat: Van norvég versenyző")
        break
else:
    print("6.feladat: Nincs norvég versenyző")

#         osszeg+=1


# if item.Orszag==0:
#     print('Nincs norvég')
# else:
#     print('Van norvég')


statisztika={}
for item in versenyzok:
    if item.Orszag in statisztika.keys():
        statisztika[item.Orszag]+=1
    else: 
        statisztika[item.Orszag]=1
print(statisztika)

for key,value in statisztika.items():
    if value >=4:
        print(f'\t{key}-{value} fő ')


