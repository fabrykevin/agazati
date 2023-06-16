# - Készítsen fv-t ami kamatos kamatot számol
# - paraméterek: összeg, hónapok száma, éves kamat

def kamatosKamat(osszeg, honapoksSzama, evesKamat):
    evekSzama = honapoksSzama / 12
    eredmeny = osszeg*((100+evesKamat)/100)**evekSzama
    return eredmeny
osszeg = float(input('Adja meg a befektett összeget: '))
honapokSzama = int(input('Adja meg a futamidőt: '))
evesKamat = float(input('Hány százalék az éves kamat:'))
print(f' Az adott futamidő után visszajáró összeg{round(kamatosKamat(osszeg, honapokSzama, evesKamat),2)}')
