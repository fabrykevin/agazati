from data import results , name ,percent, minutes, module
from fuc
 

print(f'At állományban{len(results)} vizsgázó van')


db=0
for row in results:
    
    if percent(row)>=75:
        db+=1
    print(f'{db}')

db=0
sumMinutes=0
for row in results:
    if module(row)=='Word':
        db+=1
        sumMinutes+=minutes(row)
print(f'A wordből vizsgázók átlagosan {sumMinutes/db} percet dolgoztak')


minValue = percent(results[0])
minIndex = 0
for i in range(1, len(results)):
    if  minValue>percent(results[i]):
        minValue=percent(results[i])
        minIndex=i
print(f'A legrosszabb eredményt {name(results[minIndex])} érte el: {minValue}%')



if searchByName():
    print('Volt ilyen nevu versenyzo')
else:
    print('Nem volt ilyen nevu versenyző')


        




