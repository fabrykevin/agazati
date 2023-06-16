#1.van egy 6 csapatos bajnokság.A saját csapatunk 5 meccset játszik
#kéje be a 5 meccs eredmányét pl(.:10-5->5 gollal nyert a csapat  )
#   - Írja ki,hogy hány pontja lett/van  a csapatnak(3-1-0)
#   - Írja ki a csapat jelenlegi gólkülönbségét

golkulonbseg=0
pontok=0

for i in range(1,6):
    eredmeny=input(f'{i}. mérkőzés eredménye:') #'10-5'
    golok=eredmeny.split('-')#['10','5']
    golkulonbseg+=int(golok[0])
    golkulonbseg-=int(golok[1])
    if int(golok[0])>int(golok[1]):
        pontok+=3
    elif int(golok[0])==int(golok[1]):
        pontok+=1
print(f'A csapat pontszáma {pontok}')
print(f'A csapatok gólkülönbsége:{golkulonbseg}')

    