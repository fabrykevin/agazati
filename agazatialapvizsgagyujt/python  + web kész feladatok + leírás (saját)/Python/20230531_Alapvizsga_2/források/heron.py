from math import sqrt
print('1.feladat: Háromszöh területe és kerülete')

a=float(input('a='))
b=float(input('b='))
c=float(input('c='))

Ke = a + b + c
print(f'K={Ke}')
s = Ke / 2
terulet=sqrt(s*(s-a)*(s-b)*(s-c))
print(f'T={terulet}')