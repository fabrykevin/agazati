# from feladat import prim

from ast import If
import math
from re import I


def prim(szam):
    for i in range(2,int(math.sqrt(szam))+1):
        if szam%i==0:
            return False
    return True
db=0
i=2
while db<50:
    if prim(i):
        print(i,end=' ')
        db+=1

    i+=1