import math

def terület(a, b, c): #formális paraméterke
    s=kerület/2
    return math.sqrt (s*(s-aOldal)*(s-bOldal)*(s-cOldal))#a függvény visszatér a return után megadott értékkel

def egészBekér(üzenet) -> int:
    return int(input(üzenet))



név = input('Add meg a nevedet:') #= értékadás operátora, a bal oldalon szereplő változó értékr lrgyen egyenlő
a=2+3
# = és + operátorok-műveleteket végeznek
# a, 2 , 3:operandusok
# # létrjön a b változó, mert most kap először értéket, majd belekerül az a változó értéke a b-be
#b értéke legyen egyenlő az a értékével (5)
print('Hello', név,'!')
print('Hello' +  név +'!')
print(f'hello{név}!')



print(type(név))


print('HÁROMSZÖG')
#input mindig stinget ad vissza
aOldal =egészBekér('a oldal:')#típuskonverzió!!! str->int
#print(type(aOldal))
bOldal =egészBekér('b oldal:')
cOldal =egészBekér('c oldal:')


kerület=aOldal+bOldal+cOldal
print(f'A háromszög kerülete:{kerület}')
#stringeken a + operátor összefűzést végez


terület=terület(aOldal,bOldal,cOldal) #aktuális paraméterek
print(f'A háromszög területe:{terület}')