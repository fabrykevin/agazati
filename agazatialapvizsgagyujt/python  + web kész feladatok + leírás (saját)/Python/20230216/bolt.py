#- Készítsen függvényt, aminek segítségével el lehet dönteni, hogy érdemes-e egy boltot működtetni
#	- paraméterek
#		- havi fix rezsi ktg
#		- havi bér ktg
#		- havi várható forgalom
#		- termékek átlagos haszon %-a
#	- visszatérési érték: mennyi pénz "marad" a végén
	
def bolt(rezsi,ber, forgalom,haszon):
    return (forgalom*haszon/100)-rezsi-ber

    

rezsi = int(input('Adja meg hogy mennyi rezsit fizet havonta: '))
ber = int(input('Adja meg hogy mennyi bére van: '))
forgalom = int(input('Adja meg a havi várható forgalmát: '))
haszon = float(input('Adja meg hány százalék haszon van a termékein: '))
osszHaszon=bolt(rezsi,forgalom, haszon,ber)
print(f'Az üzlet bevétele {osszHaszon}')

if osszHaszon>0:
    print('A boltot megéri működtetni a boltot.')
else:
    print('Nem éri meg működtetni a boltot.')

