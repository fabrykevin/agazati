from User import user

users:list[user]=[]

file= open('phone_book.txt', 'r', encoding='utf-8')
file.readline()
for row in file:
    users.append(user(row.strip()))
file.close()

print(f'2. feladat: A telefonkönyvben {len(users)} dolgozó szerepel.')

for item in users:
    #if'.hu' in item.email:
    if item.email[-3:]=='.hu':#eldöntés
        print('3. feladat: Van magyar e-mail cím.')
        break
else:
        print('3.feladat: Nincs magyar e-mail cím.')

name=input('4. feladat: Kérek egy nevet: ')#első találatnál megélltunk
for item in users:
    if item.name== name:
        print('\tE-mail cím:{item.email}')
        print('\ttelefonszám:{item.phone}')
        print('\tOsztály:{item.department}')
        break
else:
    print('\t Nincs ilyen nevű dolgozó')

area= input('5 feladat: Kérek egy körzetet: ') # összeset meg kell találni
found_area =False 
for item in users:
    if item.area[0:3] ==area:
        print(f'\nDolgozó neve: {item.name}. Beosztása: {item.job_title}')
        found_area=True
    if found_area==False:
        print('\t Nincs ilyen körzet.')

stat={}
for item in users:
    if item.department in stat.keys():
        stat[item.department]+=1
    else:
        stat[item.department]=1

print(f'6.feladat:30 fő feletti osztályok dolgozói:')
for key,value in stat.items():
    if value>=30:
        print(f'\t {key}: {value} fő')


file=open('managers.txt' , 'w', encoding='utf-8')
for item in users:
    if 'manager' in item.job_title:
        file.write(f'{item.name}; {item.email}\n')
file.close()


    

