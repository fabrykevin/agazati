
print('1 feladat:Téglalap területe és kerülete')
for i in range(10):
    print(f'Adja meg a {i+1} téglalp oldalait ')
    try:
        #raise ValueError('Hiba')
        a=float(input('a='))
        b=float(input('b='))
        print(f'T={a*b}')
        print(f'K={(a+b)*2}')
    except:
        print('Nem megfelelő adat!')



# def terulet(a,b):
#     ter=a*b
#     if ter<100:
#         raise ValueError('Hiba: Túl kicsi a telek!')
#     return ter

# print("feladat: Terület számítás")
# while True:
#     a=float(input('Kérem adja meg a telek szélességét (a): '))
#     if a==-1:
#         break
#     b=float(input('Kérem adja meg a telek hosszúságát (b): '))
#     if a==-1:
#         break
#     try:
#         print(f'Telek területe: {terulet(a,b)} m2')
#     except ValueError as error:
#         print(error)