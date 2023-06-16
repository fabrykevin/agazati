import math

def terület(a, b, c): # a,b,c: formális paraméterek
    s = (a+b+c) / 2
    return math.sqrt(s * (s-a) * (s-b) * (s-c)) # a függvény visszatér a return után megadott értékkel

def egészBekér(üzenet): # -> int:
    return int(input(üzenet))

név = input('Add meg a nevedet:')  # = - értékeadás operátora, a bal oldalon szereplő változó értéke legyen egyenlő a jobb oldali kifejezés értékével
# input('Add meg a nevedet:') = név - ilyen nincs
a = 2 + 3
# = és +: operátorok - műveleteket végeznek az operandusokon
# a, 2, 3: operandusok
b = a  # létrejön a b változó, mert most kap először értéket, majd belekerül az a változó értéke a b-be
# b értéke legyen egyenlő az a értékével (5)

print('Hello',név,'!')
print('Hello ' + név + '!')
print(f'Hello {név}!')

print(type(név))

print('HÁROMSZÖG')
# input mindig str-et ad vissza
# aOldal = int(input('a oldal: ')) # típuskonverzió!!! str->int
# print(type(aOldal))
# bOldal = int(input('b oldal: '))
# cOldal = int(input('c oldal: '))
aOldal = egészBekér('a oldal: ')
bOldal = egészBekér('b oldal: ')
cOldal = egészBekér('c oldal: ')

kerület = aOldal + bOldal + cOldal
print(f'A háromszög kerülete: {kerület}') 
# stringeken a + operátor összefűzést végez

terület = terület(aOldal, bOldal, cOldal) # aktuális paraméterek
print(f'A háromszög területe: {terület}')


