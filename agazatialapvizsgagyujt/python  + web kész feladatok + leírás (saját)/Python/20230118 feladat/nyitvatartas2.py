import math


ido=(input('Mennyi idó van most?' ))
ora,perc = ido.split(':')
ora=int(ora)
perc=int(perc)
idopercben=ora*60+perc
if ora >=8 and ora<16:
    megido=16*60-idopercben
    print('A bolt nyitva van.')
    print(f'Ennyi idő van még odaérni:{megido}' )
    print(f'Ennyi idő van még odaérni:{math.floor(megido/60)} : {megido%60}')
else:
    print('A bolt zárva van.')
