


data=[]
def readFile():
    file=  open('torna.csv','r', encoding='utf-8')
    firstRow=file.readline()
    #print(firstRow)
    #masodiksor=file.readline()
    #print(masodiksor)
    for row in file: #beolvassa a fájl tartalmát soronként --> row
        #print(row)
        data.append(row.strip())

    
    file.close()
    #print(data)


def getContinents():
    continents=[]
    for row in data:
        splitted=row.split(';')
        if splitted[3] not in continents:
            continents.append(splitted[3])
    return continents

def writeContinentsToFile(continents):
    file=open('continents.txt', 'w',encoding='utf-8' )
    
    for continent in continents:
        file.write(continent+'\n')

    file.close()

def writeCompetitorsFromCountryToFile(contrycode):
    file=open(contrycode + '.txt' , 'w' , encoding='utf-8')
    for row in data:
        splitted=row.split(';')
        if splitted[2].upper() ==contrycode.upper():
            file.write(splitted[1] + '\n')  
        

    file.close()

def writeTotalPointsToFile():
    file=open('totalPoints.txt', 'W')
    for row in data():
        splitted=row.split(';')
        total=float(splitted[4].replace(',','.'))+ float(splitted[5].replace(',','.'))
        file.write(splitted[1]+';'+str(total)+'\n')
    file.close()



