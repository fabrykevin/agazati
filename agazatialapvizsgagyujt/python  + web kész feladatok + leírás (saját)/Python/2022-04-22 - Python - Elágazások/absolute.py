# Menü
# 1. Abszolút érték
# 2. Százalék számítás (hányan mennek át az alapvizsgán)
# 3. Szerkeszthető-e a 3-szög


# Abszolút érték meghatározása
def absolute(number):
    if number < 0:
        # number = number * -1
        number *= -1 # van olyan is, hogy: += -= /=
    return number

# a = 5 esetén: mennyi lesz a értéke a /= 2 után: 2.5
# a = 5
# print(type(a))
# a /= 2
# print(a)
# print(type(a))

a = int(input('Kérek egy számot: '))
# print(type(a))
a = absolute(a)
print(f'A szám abszolút értéke: {a}')