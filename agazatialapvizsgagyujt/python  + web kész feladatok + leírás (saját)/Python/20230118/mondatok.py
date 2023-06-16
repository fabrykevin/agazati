import random

def névelő(szó):
    magánhangzók = 'aáeéiíoóöőuúüű'
    if szó[0].lower() in magánhangzók:
        return "az"
    return "a"
    # Egészítse ki a függvényt a visszatérést végző résszel!

def jelző():
    return random.choice(['piros', 'nagy', 'könnyed'])

print("Adjon meg három főnevet! ")
for i in range(1,4):
    noun = input(f"{i}. főnév")
    print(f"{névelő(noun)} {noun} {jelző()}")
