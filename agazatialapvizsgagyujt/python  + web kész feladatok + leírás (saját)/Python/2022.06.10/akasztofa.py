






# def betuKeres(betu,szo):
#     eredmeny=''
#     ##eredmeny='t_t__' # t betűt keressük a titkos szóban
#     for item in szo: #stringen megyünk végig, karaktereket kapunk
#         if item == betu:
#             eredmeny += betu
#         else:
#             eredmeny += '_' 
#     return eredmeny

def betuKeres2(betu, szo, allas):
    eredmeny=''
    for i in range(len(szo)):
        if szo[i]==betu:
            eredmeny+=betu
        else:
            eredmeny+=allas[i]
    return eredmeny

def keres(betu,szo):
    for item in szo:
        if item==betu:
            return True
    return False


szo= "krumpli" #string
allas=''
for item in range(len(szo)):
    allas+='_'
hibak=0

while szo !=allas and hibak < 7:
    tipp=input('Betű:')
    allas=betuKeres2(tipp,szo,allas)
    if keres(tipp, szo)==False:hibak+=1
    print(allas,"Hibák száma",hibak)

if szo==allas:
    print('Nyert')
else:
    print('Felaksztva')
    