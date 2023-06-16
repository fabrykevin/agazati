from allat import Állatfaj
allatok=[]
for i in range(3):
    faj=input('Add meg egy állatfaj nevét! ')
    tömeg=input('Hány kilogramm a tömege egy példánynak?' )
    ujallat=Állatfaj(faj, tömeg)
    allatok.append(ujallat)

legnehezebb=allatok[0]

for allat in allatok:
    if allat.tömeg>legnehezebb.tömeg:
        legnehezebb=allat

file=open('legnehezebb.txt' , 'w' , encoding='utf-8')
file.write(legnehezebb.fajnév)
file.close()





