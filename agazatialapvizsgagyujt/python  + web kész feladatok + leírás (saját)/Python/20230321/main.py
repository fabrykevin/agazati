from auto import Auto
autok: list[Auto] = []
file = open('autok.csv', 'r', encoding='utf-8')
file.readline()
for row in file:
    autok.append(Auto(row))

file.close()

print(f'2. feladat: A fájlban {len(autok)} autó szerepel.')

db = 0
for a in autok:
    if a.uzemanyag == 'Benzin':
        db += 1
print(f'3. feladat: A benzines autók aránya: {db / len(autok) * 100:.2f}%')

legjobb = autok[0]
for a in autok:
    if a.ar * a.jutalek > legjobb.ar * legjobb.jutalek :
        legjobb = a
print(f'4. feladat: A legjobb jutalékot a {legjobb.tipus} esetén {legjobb.ar * legjobb.jutalek / 100} Ft-ot érhetek el. ')


statisztika={}
for a in autok:
    if a.evjarat in statisztika.keys():
        statisztika[a.evjarat]+=1
    else:
        statisztika[a.evjarat]=1

for key, value in statisztika.items():
    print(f'{key} {value} db')


file=open('olcso.txt', 'w', encoding='utf-8')
for a in autok:
    if a.ar<8000000:
        file.write(f'{a.tipus} ;{a.marka}; {a.ar}\n')

file.close()
db=0
szin=input('7.feladat: Milyen színű autókat kerseünk? ')
for a in autok:
    if szin==a.szin:
        db+=1
        print(f'{a.tipus} {a.marka} {a.ar} \t')

if db==0:
    print('Nincs ilyen színű autó')