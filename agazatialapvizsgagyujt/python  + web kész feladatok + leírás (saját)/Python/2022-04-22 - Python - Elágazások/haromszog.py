# 3. Szerkeszthető-e a 3-szög

def szerkesztheto(aOldal,bOldal,cOldal):
    # if aOldal + bOldal > cOldal and aOldal + cOldal > bOldal and bOldal + cOldal > aOldal:
    #     return True
    # else:
    #     return False
    if aOldal + bOldal < cOldal or aOldal + cOldal < bOldal or bOldal + cOldal < aOldal:
        return False
    else:
        return True

a = int(input('a oldal: '))
b = int(input('b oldal: '))
c = int(input('c oldal: '))
if szerkesztheto(a,b,c):
    print('A háromszög szerkeszthető')
else:
    print('A háromszög NEM szerkeszthető')