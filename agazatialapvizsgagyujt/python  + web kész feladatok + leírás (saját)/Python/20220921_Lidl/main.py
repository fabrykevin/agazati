from math import floor
from random import randint
from re import I


ZARAS = 6 * 60 * 60
# ZARAS = 100
MAX_VEVO_SZAM=200
MAX_PENZTAR = 5
vevok = [] # mennyi ideje van a vevő a boltban
penztarak = [] # hány vásárló van a péztárakban
penztarakIdeje = [] # mennyi ideje nem szolgáltak ki vevőt a pénztárak

def allapotKiir(ido):
    pontosIdo = ido + 6 * 60 * 60
   #round() - matek szabályok szerint kerekít (3,5-től felfelé alatta lefelé)
   #floor() - mindig lefelé kerekít(3,7)->3
   #ceil() - mindig felfelé kerekít (3,1)->4
    ora = floor(pontosIdo / 3600)
    perc = floor((pontosIdo - ora * 3600) / 60)
    masodperc = pontosIdo - ora * 3600 - perc * 60
    print(f'Idő: {ora}:{perc}:{masodperc}')
    print(f'Vevők száma: {len(vevok)}')
    print('Vevők: ', vevok)
    print('Pénztárak: ', penztarak)
    # print('Péztárban várakozók száma: ')

def ujVevo(ido):
    if ido >= ZARAS:
        print('Bezárt a bolt, nem mehet be új vevő.')
        return
    if len(vevok) >= MAX_VEVO_SZAM:
        print('Tele van a bolt')
        return
    if randint(0,1) == 0: #érkezik új vevő 50%-os valószínűséggel
        vevok.append(0)


def vevokIdejeNovel():
    for i in range(len(vevok)):
        vevok[i] += 15

def fizetes():
    for i in range(len(penztarak)):
        if penztarakIdeje[i] <= 15: #20% valószínűséggel szolgál ki vevőt
            if randint(0,99) < 20:
                pass


def penztarNyit():
    #ha nincs egy olyan pénztár sem ahol 3-nál kevesebben vannak, akkor nyissunk újat, ha
    if len(penztarak)==MAX_PENZTAR:
        return
    for item in penztarak:
        if item < 3:
            return
    penztarak.append(0)


def penztarbolKimegy():
    #minél tüöbben vannak a pénztárban annál nagyobb valószínűséggel megy ki onnan valaki
    for i in range(len(penztarak)):
        if penztarak[i] > 5: #biztosan kimegy
            penztarak[i]-=1
        elif penztarak[i ]>4:
            if (randint(0,99)>20): #80%
                penztarak[i]-=1
        elif penztarak[i ]>3:
            if (randint(0,99)>40):#60%
                penztarak[i]-=1
        elif penztarak[i ]>2:
            if (randint(0,99)>60): #40%
                penztarak[i]-=1
        elif penztarak[i ]>1:
            if (randint(0,99)>70): #30%
                penztarak[i]-=1
        else:
            if (randint(0,99)>80): #20%
                penztarak[i]-=1

def penztarBezar():
    for i in range(len(penztarak)-1,-1,-1):
        if penztarak[i]==-1:
            del(penztarak[i])

def vevoPenztarbaMegy():
    for i in range(len(vevok)):
        if vevok[i] <30:
            pass
        elif vevok[i] > 15 and vevok[i] < 60: #20% valószínűséggel megy a pénztárba
            if randint(0,99) < 20:
                # a nyitott pénztárak közül random beáll az egyikba
                penztarak[randint(0,len(penztarak) - 1)] += 1
                #del(vevok[i])
                vevok[i]= -1 #pénztárba megy
        elif vevok[i] < 120: #40%
            if randint(0,99) < 40:
                penztarak[randint(0,len(penztarak) - 1)] += 1
                vevok[i]= -1       
        elif vevok[i] < 180: #60%
            if randint(0,99) < 60:
                penztarak[randint(0,len(penztarak) - 1)] += 1
                vevok[i]= -1
        elif vevok[i] < 240: #80%
            if randint(0,99) < 80:
                penztarak[randint(0,len(penztarak) - 1)] += 1
                vevok[i]= -1
        else: #mindeképp menjen a pénztárhoz
            penztarak[randint(0,len(penztarak) - 1)] += 1
            vevok[i]= -1
        penztarNyit()
# a pénztárba menteket törölni kell
    ujvevok=[]
    for item in vevok:
        if item !=-1:
            ujvevok.append(item)
    vevok.clear()
    for item in ujvevok:
        vevok.append (item)

def main():
    ido = 0
    penztarak.append(0) # egy pénztár nyitáskor kinyit
    while ido < ZARAS or len(vevok) > 0:
        ujVevo(ido)
        allapotKiir(ido)
        vevokIdejeNovel()
        vevoPenztarbaMegy()
        penztarbolKimegy()
        penztarBezar()
        ido += 15
        input()
    print('Bezárt a bolt, nincs benne több vevő.')

main()