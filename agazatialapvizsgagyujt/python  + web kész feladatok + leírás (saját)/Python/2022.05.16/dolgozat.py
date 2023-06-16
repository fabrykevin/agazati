from random import randint


def dolgozat(FeladatDB , elert):
    for i in range(0,FeladatDB+1):
        pont=randint(0, elert)
        print(pont, end=' ')
    print()
    
dolgozat(12,10)
print 

