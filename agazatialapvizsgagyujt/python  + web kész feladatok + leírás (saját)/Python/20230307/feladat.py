from movie import Movie

movies:list[Movie]= []

file=open('movies.csv' , 'r', encoding='utf-8')
file.readline()
for row in file:
    m=Movie(row)
    movies.append(m)

file.close()

count=0
for m in movies:
    if m.releaseyear>=1900 and m.releaseyear<2000:
        count+=1
print(f'2. feladat: {count} db film van xx.századból ')

director= input('3. feladat kérem a rendező nevét: ')
for m in movies:
    if m.director == director:
        print(f'\t {m.title}')



longestMovie=movies[0]
for m in movies:
    if longestMovie.lengthInMinutes()<m.lengthInMinutes():
        longestMovie=m

print(f'4. feladat:A leghosszabb ({longestMovie.lengthInMinutes()}perc ) filmek listája:')
 

for m in movies:
    if m.lengthInMinutes()==longestMovie.lengthInMinutes():
        print(f'\t {m.title}')

tag=input('5.feladat:Kérem adja meg a kategoriát:')
