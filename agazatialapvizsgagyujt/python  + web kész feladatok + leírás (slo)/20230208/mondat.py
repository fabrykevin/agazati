#- Olvasson be egy mondatot és alakítsa át úgy, 
#  hogy a szavak első betűje nagybetűs legyen
def capitalize(mondat: str):
    splittedData = mondat.split(' ')
    ujmondat = ''
    for item in splittedData:
        ujmondat += item.capitalize() + ' '
    return ujmondat.strip()

mondat = input("Kérem a mondatot: ")
print(capitalize(mondat))