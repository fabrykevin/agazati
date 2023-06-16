from functions import delete, load, new, search, showAll, update
from menu import menu

load()
choice = -1
while choice != 0:
    choice = menu()
    if choice == 1:
        showAll()
    elif choice == 2:
        name = input('Keresett név:')
        result = search(name)
        if len(result) == 0:
            print('Nincs ilyen ember.')
        else:
            for item in result:
                print(f'\t{item}')
    elif choice == 3:
        name = input('Új ember neve: ')
        new(name)
    elif choice == 4:
        name = input('Törlendő ember neve: ')
        delete(name)
    elif choice == 5:
        oldname = input('Mi az ember eredeti neve: ')
        if len(search(oldname)) == 0:
            print('Nincs ilyen ember.')
        elif len(search(oldname)) > 1:
            print('Túl sok találat. Pontosítson!')
        else:
            newname = input('Mi legyen az új név?: ')
            update(oldname, newname)
        # TODO: Azonos nevű embereket le kell kezelni!