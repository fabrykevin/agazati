from menu import *
from functions import *
import os
from fileHandling import *
current_directory = os.getcwd()
print('----------Üdvözöljük----------')
print('----A Sneaker Simulátorban----')
choice=-1
while choice != 0:
        if choice == 0:
            print("------Várjuk vissza!------")
        choice=menu()
        if choice == 1:
            signup(), login()
        elif choice == 2:
            #showall()
            readFile()
            #print(current_directory)
        elif choice == 3:
            Brand = input("Adja meg a cipő márkáját: ").upper()
            Type = input("Add meg a cipő típusát: ").upper()
            érték = searchSizeByType(Brand,Type)
            if érték[0] == True:
                print(f"{érték[1]}")
                méret = searchSize()
            Colour = input("Kérem a színt:").upper()
            ertek = szin(Colour)
            print(ertek)
            

        elif choice==4:
            legdrágábbcipo()
            legolcsobbcipo()
    
        elif choice==5:
            legujabbcipo()
            legregebbi()
            
        

            
            



        
            


            





      
    

   