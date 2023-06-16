from feltalalo import feltalalo
feltalaloklistaja=[]
file=open('feltalalok.txt','r' ,encoding='utf-8')

for sor in file:
    f=feltalalo(sor.strip())
    feltalaloklistaja.append(f)

file.close()
print(f'2.	feladat: A fájlban {len(feltalaloklistaja)} tudós adata szerepel ')

for felt in feltalaloklistaja:
    print(f'{felt.nev}-->{felt.talalmany}')
    
kor=int(input('4.	feladat: Kor megadása:  '))
file=open('kiiras.txt', 'w', encoding='utf-8')
for felt in feltalaloklistaja:
    if felt.halal-felt.szuletes > kor:
        print(felt.nev)
        file.write((felt.nev +'\n'))
file.close()

