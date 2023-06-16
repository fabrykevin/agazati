def maganhangzokszam(nap):
    maganhangzok='aáeéiíoóöőuúüű'
    darab=0
    for item in nap:
        if item in maganhangzok:
            darab+=1
    return darab

napok=['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']
legtobb=napok[0]
for item in napok:
    if maganhangzokszam(legtobb)<maganhangzokszam(item):
        legtobb=item

print(f'A legtöbb maganhangzó a {legtobb}-ben van')