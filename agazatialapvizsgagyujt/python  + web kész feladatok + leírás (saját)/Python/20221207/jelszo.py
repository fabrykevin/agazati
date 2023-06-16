pwd='Szivecske<3'
user='bori99'


inputUser=input('Adja meg a felhasználónevét!')
inputPwd=input('Adja meg a jelszavát!')
while pwd !=inputPwd or user !=inputUser:
    print('Belépés megtagadva.')
    inputUser=input('Adja meg a felhasználónevét!')
    inputPwd=input('Adja meg a jelszavát!')  
print('Belépés engedélyezve.')
