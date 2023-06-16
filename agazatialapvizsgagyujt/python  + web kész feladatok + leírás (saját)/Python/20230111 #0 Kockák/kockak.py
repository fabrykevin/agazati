import random
n=int(input('Hány alkalommal legyen feldobás?'))
anni=0
panni=0
for i in range(n):
    szam=random.randint(1,6)
    szam2=random.randint(1,6)
    szam3=random.randint(1,6)
    osszeg=szam +  szam2  + szam3
    
    if osszeg<10:
        nyertes='Anni'
        anni+=1
        
    else:   
        nyertes= 'Panni'
        panni+=1
     
    print(f'Dobás{szam} + {szam2}+ {szam3}= {osszeg}\t Nyert:{nyertes }') 
print(f'A játék során {anni} alkalommal Anni, {panni} alkalommal Panni nyert.')   