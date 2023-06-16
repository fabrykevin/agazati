#- Kérjen be egy egész számot, és keresse meg a nála kissebb legnagyobb prímszámot
def prim(szam):
    for i in range(2,szam):
        if szam % i == 0:
            return False
    return True


def legnagyobbPrimAmiKisebbMint(szam):
    for i in range(szam,1,-1):
        if prim(i) == True:
            return i

szam = int(input("Addjon meg egy számot: "))
print(legnagyobbPrimAmiKisebbMint(szam))