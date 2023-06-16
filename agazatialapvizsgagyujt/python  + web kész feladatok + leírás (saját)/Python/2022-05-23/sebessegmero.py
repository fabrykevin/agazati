from tracemalloc import start


print('Áthaladás 0-s km') 
start_ora=int(input('Óra: '))
start_perc=int(input('Perc: '))
start_mperc=int(input('Másopdperc: '))

km=float(input('Kapu távolsága (km):'))


print(f'Áthaladás{km}-s km')
end_ora=int(input('Óra: '))
end_perc=int(input('Perc: '))
end_mperc=int(input('Másodperc: '))

#v(km/h)=s(km)/t(h)
end_ido=end_ora+end_perc/60+end_mperc/60/60
start_ido=start_ora+start_perc/60+start_mperc/3600
eltelt_ido= end_ido-start_ido

v=km/eltelt_ido
print(f'Átlag sebesség:{v} km/h')

if v>130:
    print('Meghaladta a megengedett átlagsebességet. ment a csekk....')