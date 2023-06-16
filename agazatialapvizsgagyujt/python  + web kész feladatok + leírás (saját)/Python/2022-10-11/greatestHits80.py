
from unicodedata import name
from data import greatestHits
from functions import  publishedYear , category, durationSeconds, performer
 
# hány szám található a listában
#Legrégebbi szám címe és előadója
# leghoszabb szám hossza, megjelenés éve és kategóriája
#kérjünk egy kategóriát -->hány szám van ebből a kategóriából
                        #-->ha nincs akkor irjuk ki hogy nincs
#kérjünk be egy előadó nevet ás szerepel e a listába ha igen



print('1 feladat')
print(f'\tA listában {len(greatestHits)} dal szerepel')


def legregebbi():
    best=2000
    for hits in greatestHits:
        szamok= hits.split(';')
        if int(szamok[4]) < best:
            best=int(szamok[4])
    return best

print(legregebbi())




maxIndex = 0
maxValue = durationSeconds(greatestHits[0])
for i in range(1,len(greatestHits)):
    if maxValue < durationSeconds(greatestHits[i]):
        maxValue=durationSeconds(greatestHits[i])
        maxIndex =i
print('2.feladat : A leghosszabb szám')
print(f'\tSzám hossza:{maxValue} ')
print(f'\tMegjelenés éve:{publishedYear(greatestHits[maxIndex])}')
print(f'\tKategóriája{category(greatestHits[maxIndex])}')

categoryName =input('\t Kérem a kategória nevét')
count=0
for h in greatestHits:
    if category(h)==categoryName.upper():
        count+=1
if count==0:
    print('\tEbben a kategóriában nincs dal a listában')
else:
    print(f'{count} dal szerepel a listában ebből a kategóriából')

print('4. feladat')
name=input('\tElőadó neve')
for h in greatestHits:
    if performer(h)==name:
        print('Az elöadó szerepel a listában')
        break
else:
    print('Az előadó nem szerepel a listában')

