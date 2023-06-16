from operator import truediv


def szerkesztheto(aOldal, bOldal, cOldal):
    if aOldal+bOldal>cOldal and aOldal+cOldal>bOldal and bOldal+cOldal>aOldal
        return True
    else:
        return False
a=input('a oldal:')
b=input('b oldal:')
c=input('c oldal:')
if szerkesztheto(a,b,c):