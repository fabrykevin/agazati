from random import randint, random, randrange


def absolute(number):
    if number < 0: 
        number *= -1 
  
    return number


def atmentTanulokSzazaleka(osszesTanuloDb, bukottTanuloDb):
    if osszesTanuloDb > 0 and osszesTanuloDb >= bukottTanuloDb:
        szazalek = (1 - bukottTanuloDb / osszesTanuloDb) * 100
    else:
        szazalek = -1
    return szazalek

def szerkesztheto(aOldal,bOldal,cOldal):
    if aOldal + bOldal < cOldal or aOldal + cOldal < bOldal or bOldal + cOldal < aOldal:
        return False
    else:
        return True


# dolgozat értékelés
#bekér:pontszám(0-40% 1, 40-55% 2, 55-70 3, 70-85% 4, 85%- 5)
def dolgozatErtekeles(elertpont, osszPontszam):
    szazalek = elertpont / osszPontszam * 100
    if szazalek < 40:
        return 1
    elif szazalek< 55:
        return 2
    elif szazalek< 70:
        return 3
    elif szazalek< 85:
        return 4
    else:
        return 5



def menu():
    print('1. Abszolút érték számítás')
    print('2. Százalék számítás')
    print('3. Háromszög szerkeszthetőség')
    print('4. Dolgozat értékelés')

    valasz= input('Mit szeretne csinálni (1-4)?:')
    if(valasz == '1'):
        a = int(input('Kérek egy számot: '))
        a = absolute(a)
        print(f'A szám abszolút értéke: {a}')
    elif(valasz =='2'):
        print('Százalék számítás')
        # szazalek = atmentTanulokSzazaleka(15,3)
        osszes = int(input('Összes tanuló száma: '))
        bukott = int(input('Bukott tanulók száma: '))
        szazalek = atmentTanulokSzazaleka(osszes, bukott)
        if szazalek == -1:
            print('Hibás adatok, ebből nem számolható százalék!')
        else:    
            print(f'A tanulók {szazalek} %-a ment át a vizsgán.')
    elif valasz =='3':
  
        a = int(input('a oldal: '))
        b = int(input('b oldal: '))
        c = int(input('c oldal: '))
        if szerkesztheto(a,b,c):
            print('A háromszög szerkeszthető')
        else:
            print('A háromszög NEM szerkeszthető')
    else:
        osszes=int(input('A dolgozat összpontszáma:'))
        #elert=int(input('A dolgozat elért pontszám:'))
        elert=randint(0,osszes)
        print(f'Elért pontszám:{elert}')
        eredmeny=dolgozatErtekeles(elert,osszes)
        print(f'A dolgozat eredménye:{eredmeny}')
menu()