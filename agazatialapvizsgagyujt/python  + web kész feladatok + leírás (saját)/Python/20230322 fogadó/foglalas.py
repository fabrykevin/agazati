from adatok import adat

fogadasok:list[adat]=[]
file=open('fogado.txt', 'r', encoding='utf-8')

for row in file:
    fogadasok.append(adat(row.strip()))

file.close()


print(f'2.feladat\nFoglalások száma: {len(fogadasok)}')



nev=input('Adjon meg egy nevet: ')
splitted=nev.split(' ')
vezeteknev=splitted[0]
utonev=splitted[1]
 
db=0
for item in fogadasok:
    if item.vezeteknev==vezeteknev and utonev==item.utonev:
        db+=1

print(f'{nev} neven {db} db foglalas van')


idopont=input('Adjon meg egy érvényes időpontot ')

for item in fogadasok:
    if idopont==item.idopont:
        print(f'{item.vezeteknev} {item.utonev}')


min='2023.12.29'
legkorabbinev=''
legkorabbinev2=''
idopont=''
for item in fogadasok:
    if item.datum<min:
        min=item.datum
        legkorabbinev=item.vezeteknev
        legkorabbinev2=utonev

    
