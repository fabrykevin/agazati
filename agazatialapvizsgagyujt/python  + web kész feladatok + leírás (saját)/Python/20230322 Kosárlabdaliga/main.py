from adatok import adat

eredmenyek:list[adat]=[]

file=open('eredmenyek.txt', 'r', encoding='utf-8')

file.readline()
for row in file:
    eredmenyek.append(adat(row.strip()))

file.close()

count=0
print('\n3.feladat:\n')
for item in eredmenyek:
    if item.hazai=='Real Madrid':
        count+=1
print(f'A Real Madrid Hazai {count} meccset játszott')

db=0
for item in eredmenyek:
    if item.idegen=='Real Madrid':
        db+=1

print(f'A Real Madrid Idegen: {db} meccset játszott')

print('\n4.feladat:\n')
db=0
for item in eredmenyek:
    if item.hazai_pont==item.idegen_pont: 
        db+=1 
    if db>0:
        print(f'{db} db döntetlen meccs volt')
else:
    print(f'Nem volt döntetlen mérkőzés')



print('\n5.feladat\n')
csapat = ""
for item in eredmenyek:
    if "Barcelona" in item.hazai:
        csapat = item.hazai
    elif "Barcelona" in item.idegen:
        csapat = item.idegen
print(csapat)




print('\n6.feladat:\n')

for item in eredmenyek:
    if item.időpont=='2004-11-21':
        print(f"{item.hazai}-{item.idegen}({item.hazai_pont}:{item.idegen_pont})\t")

print('\n7.feladat:\n')
statisztika={}

for item in eredmenyek:
    if item.helyszín in statisztika.keys():
        statisztika[item.helyszín]+=1
    else: 
        statisztika[item.helyszín]=1

for key, value in statisztika.items():
        if value>20:
            print(f' {key}, {value}') 


file=open('eredmeny3.txt', 'w', encoding='utf-8')
for item in eredmenyek:
    item.hazai_pont>70
file.write(f'{item.hazai} ;{item.idegen}; {item.hazai_pont}:{item.idegen_pont}')


file.close()

