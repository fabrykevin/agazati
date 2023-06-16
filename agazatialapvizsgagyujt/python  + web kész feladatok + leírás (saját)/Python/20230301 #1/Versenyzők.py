from adatok import adat
pilotak:list[adat]=[]

file=open('pilotak.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    pilotak.append(adat(row.strip()))

file.close()

print(f'3.feladat: {len(pilotak)}')


print(f'4.feladat: {pilotak[-1].nev}')
print('5.feladat:')
for i in pilotak:
    if i.születési_dátum<='1901.01.01':
        print(f' \t {i.nev}\t{i.születési_dátum}')


#for item in pilotak:
#    if item.ev<1901:
#        print(f'\t {item.nev} {item.születési_dátum}')



min=99999999
nemzetiseg=0
for item in pilotak:
    if item.rajtszám !='':
        if int(item.rajtszám)<=min:
            min=int(item.rajtszám)
            nemzetiseg=item.nemzetiség
print(f'6.feladat:{nemzetiseg}')





# min=99999999
# minIndex=0
# for index,item in enumerate(pilotak):
#     if item.rajtszám !='':
#         if int(item.rajtszám)<=min:
#             min=int(item.rajtszám)
#             minIndex=index
#             print(f'6.feladat:{pilotak[minIndex].nemzetiség} {pilotak[minIndex].nev}')



statisztika = {}

for item in pilotak:
    if item.rajtszám in statisztika.keys():
        statisztika[item.rajtszám]+=1
    else:
        statisztika[item.rajtszám]=1

x=[]

for key,value in statisztika.items():
    if value >=2 and key !='':
        x.append(key)
        print(','.join)
    



    print(statisztika)




    
