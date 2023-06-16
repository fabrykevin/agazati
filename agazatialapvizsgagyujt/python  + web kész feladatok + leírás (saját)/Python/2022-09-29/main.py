
from fuggvenyek import highestPower, lowestConsumption, searchPlate,totalPrice,countBrand,averageAge

plate=input("Kérek egy rendszámot:")
if searchPlate (plate):
    print('Van ilyen rendszám a nyilvántartásban')
else:
     print('Nincs ilyen rendszám a nyilvántartásban')

print(f'A flotta összértéke: {totalPrice()}')

print(f'A flotta átlagéletkora: {averageAge ()}')

brand=input('Kérek egy márkát:')
print(f'{countBrand(brand)}darab {brand} márkájú autó van')

print(f'A legerősebb auto teljesítménye:{highestPower()}LE')

print(f'A legnkisebb fogyasztású autó{lowestConsumption()}')