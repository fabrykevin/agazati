from feltalalo import feltalalo

feltalalokListaja = []

file = open('feltalalok.txt', 'r', encoding='utf-8')
for sor in file:
    f = feltalalo(sor.strip())
    feltalalokListaja.append(f)

file.close()

print(f'2.feladat: A fájlban {len(feltalalokListaja)} tudós adata szerepel ')
print(f'3.	feladat: feltalálók-találmányok ')
for felt in feltalalokListaja:
    print(f'{felt.nev}->{felt.talalmany}')

kor = int(input('4. feladat: Kor megadása: '))
file = open('kiiras.txt', 'w', encoding='utf-8')
for felt in feltalalokListaja:
    if felt.halal - felt.szuletes > kor:
        print(felt.nev)
        file.write(felt.nev + '\n')

file.close()