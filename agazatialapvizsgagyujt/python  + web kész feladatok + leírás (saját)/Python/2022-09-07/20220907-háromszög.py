#Kérjünk be 3 valós számot


from math import sqrt


a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))

if a + b > c and b + c > a and a + c > b:
    print('A megadott adatokkal szerkezthető 3szög')

    print('Kerület', a + b + c)

    s=  (a+b+c)/2
    T=sqrt(s*(s-a)* (s-b)*(s-c))
    print('Terület:', T)
else:
    print('A megadott adatokkal NEM szerkezthető 3szög')

