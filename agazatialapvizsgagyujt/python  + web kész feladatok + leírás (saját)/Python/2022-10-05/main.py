from functions import *

print(f'A versenyen{countCompetitors()} versenyző indult.')
parallelBarsWinner=winner('Korlát')
print(f'Korláton a győztes pontszám {parallelBarsWinner}')
jumpWinner=winner('Ugrás')
print(f'Ugrásban győztes {jumpWinner}')

StartNumber= input('Rajtszám:')
ringResult=ringResult(StartNumber)
if ringResult==False:
    print('Nincs ilyen rajtszámú versenyző')
else:
    print(f'A versenyző gyűrűn elért eredménye: {ringResult}')

print(f'A lólengésben kiesett: {countlessTehnPommelHorse(14.5)} fő')

print('Földrészek ahonnan jöttek: ')
print(regions())

countCompetitiorsOfCountries()