# - Olvasson be egy szót, és írja ki a betűit egy sorba, egymástól szóközzel elválasztva.
# ALMA -> A L M A

def szoRitkit(szo):
    ujszo = ''
    for betu in szo:
        ujszo += betu + ' '
    return ujszo.strip()

szöveg = input('Kérek egy szót!: ')
print(f'"{szoRitkit(szöveg)}"')