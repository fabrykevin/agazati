
from functions import *  #delete, load, new, search, searchWithIndex, showall, update, updateByIndex
from menu import menu
load()
choice=-1
while choice != 0:
    choice=menu()
    if choice == 1:
        showall()
    elif choice == 2:
        name=input('Keresett név:')
        result=search(name)
        if len(result)==0:
            print('Nincs ilyen ember.')
        else:
            for item in result:
                print(f'\t{item}')
    elif choice == 3:
        name=input('Új ember neve: ')
        new(name)
    elif choice == 4:
        name=input('Törlendő ember neve: ')
        delete(name)
    #elif choice == 5:
     #   name=input('Kérem a változtatni kívánt nevet: ' )
      #  newname=input('Kérem a nevet: ')
       # update(name , newname)
        

   # elif choice == 5:
    #    oldname= input('Mi az ember eredeti neve:  ')
    #if len(search(oldname))==0:
     #   print('Nincs ilyen.')
    #elif len(search(oldname))>1:
     #   print('Túl sok találat, Pontosítson!  ')
    #else:
     #   newname=input('Mi legyen az új név ')
     #   update(oldname, newname)
    elif choice == 5:
        oldname= input('Mi az ember eredeti neve:  ')
        results=searchWithIndex(oldname)
        if len(results)==0:
            print('Nincs találat')
        else:
            for index in results:
                print(f'\t{index} - {names[index]}')
            userIndex= input('Adja meg a választott ember sorszámát: ')
            if userIndex not in results:
                print('Nincs ilyen sorszám!')
            else:
                newname=input('Mi legyen az új név?: ')
                updateByIndex(userIndex, newname)