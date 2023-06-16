from filmalap import oraperc
for i in range(3):
    film=input('Add meg egy film címét!')
    hossz=int(input('Hány perces a film?'))
    print(f'{film} film {oraperc(hossz)} hosszú.')