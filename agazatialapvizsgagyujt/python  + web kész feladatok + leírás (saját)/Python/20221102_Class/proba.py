
from Result import Result
results=[]
res1=Result() #Példányosítás=Result osztályból létrehozok egy osztálypéldányt
res1.name='Kovács Béla'
res1.module='Excel'
res1.time='41:41'
res1.result=30

results.append(res1)

print(res1)
print(res1.name)
print(res1.time)

print(results)



res2=Result()
res2.name='Takács Béni'
res2.module='Powerpoint'
res2.time='40:40'
res2.result=20

results.append(res2)
print(results)
for item in results:
    print(f'{item.name}- {item.time}')


