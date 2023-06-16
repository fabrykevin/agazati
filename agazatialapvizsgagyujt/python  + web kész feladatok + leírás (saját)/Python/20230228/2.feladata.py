# diák nevének bekérése
nev = input("Kérlek, add meg a diák nevét: ")

# az öt tantárgy nevének és jegyeinek bekérése
tantargyak = ["matek", "magyar", "angol", "történelem", "fizika"]
jegyek = []
for tantargy in tantargyak:
    jegyek.append(int(input(f"{tantargy} jegye: ")))

# az átlagok kiszámítása és az osztályzatok meghatározása
atlagok = []
for jegy in jegyek:
    atlagok.append(jegy / 2)
osztalyzatok = []
for atlag in atlagok:
    if atlag >= 4.5:
        osztalyzatok.append(5)
    elif atlag >= 3.5:
        osztalyzatok.append(4)
    elif atlag >= 2.5:
        osztalyzatok.append(3)
    else:
        osztalyzatok.append(2)

# az év végi átlag és az ösztöndíj meghatározása
ev_vegi_atlag = sum(atlagok) / len(atlagok)
if ev_vegi_atlag >= 4.5:
    osztondij = 100000
elif ev_vegi_atlag >= 4.0:
    osztondij = 50000
elif ev_vegi_atlag >= 3.5:
    osztondij = 30000
else:
    osztondij = 0

# eredmények kiírása
print(f"{nev} év végi jegyei:")
for i in range(len(tantargyak)):
    print(f"{tantargyak[i]}: {osztalyzatok[i]}")