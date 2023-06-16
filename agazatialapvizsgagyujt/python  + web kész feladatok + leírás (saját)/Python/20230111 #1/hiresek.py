from hiresek_alap import Celeb
celebek=[]
def mentesFajlba():
    fajl=open('celebek.txt', 'w' ,encoding='utf-8')
    for celeb in celebek:
        fajl.write(f'{celeb.nemzetiseg()} {celeb.name} egy híres{celeb.job} \n')

    fajl.close()




for i in range(3):
    celeb=Celeb()
    celeb.name=input('Add meg egy híres nő nevét!' )
    celeb.job=input('Add meg a foglalkozását!' )
    celeb.nationality=input('Add meg a nemzetiségét (a/n)!' )
    celebek.append(celeb)


for c in celebek:



    print(f'{celeb.nemzetiseg()} {celeb.name} egy híres{celeb.job} ')

mentesFajlba()