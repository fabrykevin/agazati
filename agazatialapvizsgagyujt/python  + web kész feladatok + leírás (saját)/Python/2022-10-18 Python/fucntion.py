from data import results

def sikeres():
    suma = 0
    for result in results:
        adatok = result.split(";")
        if int(adatok[3]) >= 75:
            suma +=1
    return suma

# def legjobb():
#     legjobb_diak=""
#     pont = 0
#     for result in results:
#         adatok = result.split(";")
#         if int(adatok[3]) > int(pont):
#             pont = int(adatok[3])
#             legjobb_diak = adatok[0]
#     return legjobb_diak,pont

def legrosszabb():
    legrossabb_diak=""
    pont = 101
    for result in results:
       adatok = result.split(";")
       if int(adatok[3]) < int(pont):
           pont = int(adatok[3])
           legrosszabb_diak = adatok[0]
    return legrosszabb_diak,pont

def word():
    darab = 0
    osszesido = 0
    for result in results:
       adatok = result.split(";")
       if adatok[1] =="Word":
            darab +=1
            osszesido += float(adatok[2].replace(":","."))
    return osszesido/darab

def searchByName(name):
    for result in results:
        adatok = result.split(";")
        if name == adatok[0]:
            return True,adatok[1],adatok[2],adatok[3]
    False 
