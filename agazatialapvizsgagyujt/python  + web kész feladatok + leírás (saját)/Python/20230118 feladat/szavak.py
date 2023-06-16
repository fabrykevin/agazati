elsoszo=input('Adj meg egy szót!')
masodik=input('Adj meg egy másik szót!' )
if len(elsoszo)> len(masodik):
    print(f'A hosszabb szó:{elsoszo}' )
elif len(masodik)>len (elsoszo):
    print(f'A hosszabb szó:{masodik}' )
else:  
    print('A két szó egyforma hosszú.')


