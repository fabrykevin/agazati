
from random import randint, random


tippek = []
hazai = []
vendeg = []


def tippBeker():
    #1,2,x,X
        tipp=""
        while not(tipp=='1' or tipp=='2' or tipp=='x'):
            tipp = input('Kérem a tippet (1,2,x):').lower()
        return tipp

def eredmenyGeneral():
    #max 9 gol lehet
    for i in range(14):
        hazai.append(randint(0,9)) 
        vendeg.append(randint(0,9))

def golokbolEredmeny(hazaiGol, VendegGol):
    if hazaiGol > VendegGol:
        return '1'
   
    elif hazaiGol == VendegGol:
        return 'x'
   
    else:
        return '2'




def talaltE(tipp, hazaiGol, vendegGol):
    return tipp == golokbolEredmeny(hazaiGol, vendegGol)

def talalatokSzama():
    talalatokDarab = 0
    for i in range(14):   
         if  talaltE(tippek[i], hazai[i], vendeg[i]):
            talalatokDarab +=1
    return talalatokDarab




def kiir():
    for i in range (14):
        print(f'{tippek[i]}\t{hazai[i]}-{vendeg[i]}\t{golokbolEredmeny(hazai[i], vendeg[i])}')


    



def osszesTippBeker():
  for i in range (14):
        tippek.append(tippBeker())


def main():
    osszesTippBeker()
    eredmenyGeneral()
    print('Tipp\tGólkülönbség\tEredmény')
    print('Eredmenyek')
    kiir()
    print(f'Végeredmény{talalatokSzama()} darab találat.')
main()