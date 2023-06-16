from epitmeny import epitmeny

epitmenylista :list[epitmeny] = []
A = 0
B = 0
C = 0 



def beolvas():
    file=open('utca.txt', 'r', encoding='utf-8' )
    splitted=file.readline().strip().split(' ')
    global A,B,C
    A = int(splitted[0])
    B = int(splitted[1])
    C = int(splitted[2])
    for sor in file:
        e=epitmeny(sor.strip())
        epitmenylista.append(e)
    file.close()


def kereses(adoszam):
    talalt=False
    for et in epitmenylista:
        if et.adoszam== adoszam:
            print(f'{et.utca} utca {et.hazszam}')
            talalt=True
    if talalt !=True:
        print('Nem szerepel az adatállományban')

def ado(adosav, alapterulet):
    ado=0
    if adosav=='A':
        ado= A*alapterulet
    elif adosav=='B':
        ado=B*alapterulet
    elif adosav=='C':
        ado=C*alapterulet
    if ado<10000:
        return 0
    else:
        return ado





beolvas()
print(f'2. feladat. A mintában {len(epitmenylista)} telek szerepel.' )
adoszam = input('3. feladat. Egy tulajdonos adószáma:')
kereses(adoszam)
print(f"Egy 500 negyzetméters A kategoriás telek adója {ado('A', 500)}")






    
