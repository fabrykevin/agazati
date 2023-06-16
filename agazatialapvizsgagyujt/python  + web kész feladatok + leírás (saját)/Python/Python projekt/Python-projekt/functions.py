from result import Result
from fileHandling import *
data=[]
def readFile():
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    for row in file:
        data.append(row.strip().split(";"))
    print(* data, sep = "\n")
    file.close

def showall():
    print('Összes cipő')
    for row in data:
        print(row, end=' ')
def login():
    print('Bejelentkezés')
    user=input('Felhasználónév:')
    pwd=input('Jelszó:')
    f=open('nevek.csv', 'r'  )
    for line in f.readlines():
        us,pw =line.strip().split(';')
        if (user in us) and (pwd in pw):
            print('Sikeres')
            return True

def signup():
    file=open('nevek.csv', 'a', encoding='utf-8')
    print('Regisztráció')
    username=input('új Felhasználónév:')
    password=input('új jelszó:')
    term=input(' elfogadás/elutasítás: ')
    if term=='elfogadás':
        print('regisztráció sikeres')
        file.write(f'{username}; {password} \n')
    elif term=='elutasítás':
        print('sikertelen regisztráció')
    else:
        print('Nincs ilyen opció')

def legdrágábbcipo():
    file=open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    legnagyobb=0
    nev =""
    neve=""
   
    for row in file:
        splitted=row.split(';')
        
        if int(splitted[6])> legnagyobb:
            legnagyobb=int(splitted[6])
            nev = splitted[2]
            neve=splitted[1]
    print(f"A legdrágább cipő neve {neve} {nev} és az ára {legnagyobb} dollár") 
    file.close()

def legolcsobbcipo():
    file=open('Sneaker.csv', 'r' , encoding='utf-8')
    file.readline()
    legkisebb=9999999
    nev = ""
    neve=""
    for row in file:
        splitted=row.split(';')
        if int(splitted[6])< legkisebb:
            legkisebb=int(splitted[6])
            nev = splitted[2]
            neve=splitted[1]
    file.close()
    print(f"A legolcsobb cipő neve {neve} {nev} és az ára {legkisebb} dollár")



def legujabbcipo():
    file=open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    legnagyobb=0
    nev=''
    neve=""
    for row in file:
        splitted=row.strip().split(';')
        if int(splitted[7])> legnagyobb:
            legnagyobb=int(splitted[7])
            nev=splitted[2]
            neve=splitted[1]
            
    file.close()
    print(f"A legújabb cipő neve {neve} {nev} és a megjelenési dátuma {legnagyobb}")
    



def legregebbi():
    file=open('Sneaker.csv', 'r' , encoding='utf-8')
    file.readline()
    legkisebb=9999
    nev=''
    neve=""
    for row in file:
        splitted=row.strip().split(';')
        if int(splitted[7])< legkisebb:
            legkisebb=int(splitted[7])
            nev=splitted[2]
            neve=splitted[1]
    file.close()
    print(f"A legrégibb cipő neve {neve} {nev} és a megjelenési dátuma {legkisebb} ")


#def brandSearch():
 #   file = open('brand.csv', 'a', encoding='utf-8')
  #      file.write()



def szin(Colour):
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    for row in file:
        splitted = row.strip().split(';')
        if splitted[3].upper() == Colour:  
            return splitted[4]
    return False

def searchSizeByType(Brand,Type):
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    file.readline()
    for row in file:
        splitted = row.strip().split(';')
        if splitted[1].upper() == Brand and splitted[2].upper() == Type:
            return splitted[4]
    return False

méret = []

def searchSize():
    file = open('Sneaker.csv', 'r', encoding='utf-8')
    for row in file:
        splitted = row.strip().split('.')
        méret.append(row)
        print(méret)




