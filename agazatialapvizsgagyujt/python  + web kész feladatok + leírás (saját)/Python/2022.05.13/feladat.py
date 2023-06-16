import random
print("Gondoltam egy számra")
number=random.randint(0,100)
inputnumber= None
probak=1


def checkNumber(szam):
    global number
    global probak

    if szam>=0 and szam<=100:
        if szam <number:
            print("túl kicsi")
            probak +=1
        elif szam>number:
            print("túl nagy")
            probak +=1
        else:
            print("A szám legyen 0 és 100 között")
        return  probak
    while inputnumber !=number:
        inputnumber=int(input(""))
        checkNumber(inputnumber)

    print(" Eltaláltad")
    print(f"A szám{number} volt")
    print(f"{probak}-od volt")