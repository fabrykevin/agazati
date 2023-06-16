from NFL import NFLadatok

Adatok:list[NFLadatok]=[]


file=open('NFL_iranyitok.txt', 'r',encoding='utf-8' )

file.readline()

for row in file:
    Adatok.append(NFLadatok(row.strip()))

file.close()

print(f'3.feladat: A statisztikában {len(Adatok)} irányító szerepel')

# for item in Adatok:
for item in Adatok:
    if item.yard()>4000 and item.iranyitomutato>=100:
        print(f'Neve{item.nev} {item.iranyitomutato} {item.kiserletek}' )
        
        
   #      print(f'5.feladat: Legjobb irányítók:\n {item.nev}(Irányító mutató: {} , passzok{}m)')
eladottlabdak=int(input('6.feladat:Eladott labdák száma:'))
file2=open('A legtobbeladott.txt ' , 'w', encoding='utf-8')
for item in Adatok:
    if eladottlabdak>item.eladott:
        file2.write(f'{item.nev}\n')
        

maxNev=''
max=0
for item in Adatok:
    if item.TDpasszok>max:
        item.TDpasszok=max
        maxNev=item
print(f'7.feladat:{item.nev},{item.eladott}, {item.TDpasszok} ')        

        
print('8.feladat:Legsikeresebb egyetemek:')

stat={}
for item in Adatok:
    if item.egyetem in stat.keys():
        stat[item.egyetem]+=1
    else:
        stat[item.egyetem]=1

for key, value in stat.items():
    if value>1:
        print(f'\t{key} - {value} db')
    