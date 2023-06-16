from math import floor
from random import randint


ZARAS=100
MAX_PENZTAR=5
vevok=[] #mennyi ideje van a boltban
penztarak=[] #hány vásárló van a pénztárban
penztarakIdeje=[] #mennyi ideje nem szolgáltak ki vevőt a pénztárak
def allapotKiir(ido):
    pontosIdo =ido+6*60*60
    ora= floor( pontosIdo/3600)
    perc =floor((pontosIdo-ora*3600)/60)
    masodperc=pontosIdo-ora*3600-perc*60
    print(f'Idő:{ora}:{perc}:{masodperc}')
    print(f'Vevők száma:{len(vevok)}')
    print('Pénztárban várakozók száma:')
    print('Vevők', vevok)
    print('Pénztárak', penztarak)   



def ujVevo(ido):
  if ido > ZARAS:
      print('Bezárt a bolt , nem mehet be új vevő.')
      return
  if len(vevok)>=200:
      print('Tele van a bolt')
      return
  if randint(0,1)==0: #megérkezik az új vevő
            vevok.append(0)

def vevokIdejeNovel():
    for i in range (len(vevok)):
        vevok[i] += 15

def fizetes():
   for i in range (len(penztarak)):
    if penztarakIdeje[i]<=15: #20% valószínűséggel szolgál ki vevőt
        if randint(0,99)<20:
            pass
def vevoPenztarbaMegy():
    for i in range (len(vevok)):
        if vevok[i]>60 and vevok[i]<60: #20% valószínűséggel megy a pénztárba
            if randint(0,99)<20:
                #nyitott pénztárok közül random beállunk az egyikne
                penztarak[randint(0,len(penztarak)-1)] +=1
        elif vevok[i]< 120: #40%
            if randint(0,99)<40:
                penztarak[randint(0,len(penztarak)-1)] +=1
        elif vevok[i]< 180: #60%
            if randint(0,99)<60:
                  penztarak[randint(0,len(penztarak)-1)] +=1
        elif vevok[i]< 240: #80%
            if randint(0,99)<80:
                penztarak[randint(0,len(penztarak)-1)] +=1

        else:#MINDEKÉPP MENJEN A PÉNZTÁRHOZ  100%
            penztarak[randint(0,len(penztarak)-1)] +=1
            

                

def main():
    ido=0
    penztarak.append(0) # egy pénztár nyitáskor kinyit
    while ido < ZARAS or len(vevok)>0:
        ujVevo(ido)
        allapotKiir(ido)
        vevokIdejeNovel()
        ido += 15
        input()
    print('Bezárt a bolt, nincs benne több vevő')
main()