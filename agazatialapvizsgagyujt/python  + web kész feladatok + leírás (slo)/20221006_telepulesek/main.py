from functions import legkisebb, legtobbLakosuKozseg, nagykozsegek, telepulesTersege, telepulesekSzama, osszesLakos, zahonyi1500

print(f'Települések száma Szabolcs-Szatmár-Bereg megyében: {telepulesekSzama()} db')

# Határozza meg és írja ki a képernyőre Szabolcs-Szatmár-Bereg Megye lakosságát! 
print(f'A megye lakossága: {osszesLakos()} fő')

# Keresse meg és írja ki a képernyőre a megye legkisebb területű települését!
print(f'A legkisebb település: {legkisebb()}')

# Határozza meg és írja ki, hogy a nagyközségből hány található a megyében!
print(f'A megyében {nagykozsegek()} darab nagyközség található.')

# Kérjük be egy település nevét és határozzuk meg, hogy melyik térségben van!
telepules = input('Település neve: ')
terseg = telepulesTersege(telepules)
if terseg == False:
    print('Nincs ilyen nevű település')
else:
    print(f'{telepules} a {terseg} térségben található.')

# Határozzuk meg, hogy a Záhonyi térségben hány darab 1500ha feletti teleülés található!
print(f'A Záhonyi térségben {zahonyi1500()} darab 1500ha feletti teleülés található')

# Melyik községben laknak a legtöbben?
print(f'{legtobbLakosuKozseg()} községben laknak a legtöbben')