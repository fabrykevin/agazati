import random
x=input('Első játékos neve:' )
y=input('Második játékos neve:')
while True:
    dob1 = random.randint(1, 6)
    dob2 = random.randint(1, 6)
    if dob1 == 6 and dob2 == 6:
        
        print(f"A játékot ")
    else:
        print("Dobás eredménye: ", dob1, dob2)
    
    print(f'{y}, \n{x} {dob1}, {dob2}')
