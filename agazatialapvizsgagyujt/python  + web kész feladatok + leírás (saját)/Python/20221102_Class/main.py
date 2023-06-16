
from create import addResult
from fileHandling import loadData, saveResult
#from listAll import listAll
from menuk import menu
from search import searchByName, searchByName2 , searchUnder


results=loadData()
#print(results)
#print(f' vizsgázók száma: {len(results)}')
#print(f'Első vizsgázó {results[0].name}')
#print(f'Első vizsgázó ideje {results[0].time}')

results=loadData()
choice=''
while choice != 0:
    choice =menu()
    if choice ==1:
      #  listAll()
    #elif choice==2:


        name=input('Tanuló neve: ')
        found=searchByName2(results, name)
        if found != False:
            print(f'{found.name} eredménye {found.module} modulból: {found.result} pont, {found.time} idő alatt.')

else:
    choice==3

res=addResult()
results.append(res)
saveResult(res)



name=input('Tanuló neve: ')
index=searchByName(results, name)
if index != False:
    print(f'{results[index].name} eredménye {results[index].module} modulból: {results[index].result} pont, {results[index].time} idő alatt.')


found=searchByName2(results, name)
if found != False:
    print(f'{found.name} eredménye {found.module} modulból: {found.result} pont, {found.time} idő alatt.')


failed=searchUnder(results, 50)
print('Bukottak listája:')
for item in failed:
    print(f'\t{item.name} - {item.result} pont')
