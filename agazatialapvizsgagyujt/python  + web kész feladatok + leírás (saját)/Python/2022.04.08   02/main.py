# Kiírja a szöveget - comment Ctrl+K+C vissza:Ctrl+K+U
from signal import alarm


print("Peter's alma")
print('hello')

szam = 2
print(szam)

a = 2
b = 3
c = a + b
print(c)

print(f'c változó értéke={c}')
print('c értéke= ',c)
print(a,'+',b,'=',c)#2+3=5
print(f'{a} + {b}= {c}')

név = "Péter"
#változó név szabálya
#1péter - nem kezdődhet számmal
#péter - neve nem lehet benne szóköz
#Peters' name nem lehet benne speciális karakter sem. csak a-z vagy A-Z vagy 0-9 vagy _ 
#péter1=12- ez jó 
#case sensitive- nagy betűk és a kis betűk különbözőek
A=3
a=3
#'Alma' nem egyenlő 'alma'
#Olyan változónevet kell változtatni, ami utal annak tartalmára
#asd = 12 - TILOS
#a=1
#b=20
#c=321
#d=körte
#e=true


a=2
print(a)
a=5
print(a)

#Autó:típus, tulajdonos
autó_típus='Opel'
autó_tulajdonos='Gipsz Jakab'

autóTípus='Lada' #camel case

AutóTípus='BMW' #Pascal case

print(type(a))# int-egész szám
a='alma'
print(type(a))# str- string (szöveg)

a=3.14
print(type(a))# float. lebegőpontos (valós) szám


print('\tTabulátorral kezdődő sor')
print('\t\tTabulátorral kezdődő sor')
print('alma', 'körte', 'narancs', sep'-' end'='  )