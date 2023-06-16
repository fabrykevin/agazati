from signal import valid_signals


def alkohol(mennyiseg_dl,vol):
    return mennyiseg_dl*vol*0.8


suly=int(input("testsúly(kg)?:"))
valasz=-1
verezrelek=0
while valasz !=0:
    print('Ital lap')
    print('0-semmit')
    print('1-sör(0,51)5%')
    print('2-Bor(0,51)10%')
    print('3-Vodka(0,051)40%') 
    valasz =int(input('Mit szeretne?:'))
    if valasz==1:
        verezrelek += alkohol(5,5) / suly
    elif valasz==2:
        verezrelek += alkohol(2,10) / suly
    elif valasz==3:
        verezrelek += alkohol(0.5,40) / suly 
print(f'Véralkohol szintje:{verezrelek}')
if verezrelek<0.3:
    print('Még nincsenek tünetek')
elif verezrelek<0.5:
    print('Az első tünetek megjelenése, csillogó szem, derűsebb hangulat, bőbeszédűség, gátlások kezdeti leépülése, reflexek tompulása.')
elif verezrelek<1.5:
    print('Ittasság. Eufória, kifejezetten emelkedett hangulat, gátlások elvesztése, alaptalan önbizalom, erősödő logorrhoea (bőbeszédűség, "szómenés"). Mozgáskoordináció romlása, növekvő reakcióidő, szűkülő térlátás, belövellt kötőhártya. Pulzus és légzés szaporább, vérnyomás emelkedik, verejtékezés, fokozott vizeletkiválasztás (diuresis).')
elif verezrelek<2.5:
    print('Részegség. Excitáció (izgatottság), egzaltáció, nyugtalanság, ingadozó hangulat, agresszivitás. Normák figyelmen kívül hagyása. Érzékelés, reflexek, egyensúlyérzés számottevő romlása, bizonytalan járás és térbeli tájékozódás, akadozó beszéd. Sápadtság, légzés és szívműködés gyérül, hányinger, hányás jelentkezhet.')
elif verezrelek<4:
    print('Alkoholmérgezés. Zavarodottság, aluszékonyság, később komatózus szak: ingerekre nincs reakció, reflexek nem válthatóak ki, pupillák szűkek (romló kilátások, ha ezután kitágul), légzés felületes, pulzus gyenge, vérnyomás alacsony. Vizelet- és széklettartási nehézségek. Aspiráció, fulladás veszélye (garatreflex nincs, nyelv hátracsúszhat), szabadban kihűlés, fagyás. Életveszélyes állapot.')
else:
    print('Halál')
