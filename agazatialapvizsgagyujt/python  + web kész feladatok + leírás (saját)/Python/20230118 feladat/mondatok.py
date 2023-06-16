import random
def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhangzók:
        return 'az'
    else:
        return'a'
    # Egészítse ki a függvényt a visszatérést végző résszel!


def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

print('Adja meg a három főnevet:!')
for i in range(3):
    fonev=input(f'{i+1}. főnév: ')
    print(f'{névelő(fonev)} {fonev} {jelző()}')
