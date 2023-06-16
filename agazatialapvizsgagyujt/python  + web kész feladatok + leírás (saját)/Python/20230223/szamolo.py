import random
valasz=input('Milyen műveletet szeretne gyakorolni? \n1.Összeadás \n2.Kivonás \n3.Szorzás  ' )
db=0
ok=0
while ok !=5:
    db+=1
    a=random.randint(1,10)
    b=random.randint(1,10)
    if valasz==1:
        d=a+b
        c=int(input(f'Adja össze {a} és {b}t: '))
    elif valasz==2:
        d=a-b
        c=int(input(f'Vonja ki{a} és {b}t: '))
    elif valasz==3:
        d=a*b
        c=int(input(f'Szorozza össze{a} és {b}t: '))
    if d==c:
        ok+=1
        print('Helyes')
    else:
            
        print('Hibás')

        
            






print('Gratulálunk! \n Sikerült 5 helyes műveletet elvégezni 8 próbálkozásból. ')







