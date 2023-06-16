from data import results
from fucntion import *

print(f"{len(results)}db vizsgázó van")
print(f"{sikeres()} diák ment át")
# print(f"{legjobb()[0]} {legjobb()[1]}-al a legjobb")
print(f"{legrosszabb()[0]} {legrosszabb()[1]} al a legrosszabb")
print(f"átlagosan{word()} volt az idő word alatt")


name = input("Adjon meg egy nevet")
if searchByName(name)[0] == True:
    print(f"{name}-nek {searchByName(name)[1]} ecdl dolgozata van,{searchByName(name)[2]} idővel és{searchByName(name)[3]} %")
else:
    print(f"{name} nem létezik")