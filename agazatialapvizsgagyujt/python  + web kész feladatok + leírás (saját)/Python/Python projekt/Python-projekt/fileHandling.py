from result import Result

def loadData():
    Sneakers = []

    file = open('Sneaker.csv', 'r', encoding='utf-8')

    file.readline()
    for row in file:
        splitted = row.split
        snkr = Result()
        snkr.Code = splitted[0]
        snkr.Brand = splitted[1]
        snkr.Type = splitted[2]
        snkr.Colour = splitted[3]
        snkr.Size = splitted[4]
        snkr.Sex = splitted[5]
        snkr.Price = splitted[6]
        snkr.Year = splitted[7]
        
        Sneakers.append(snkr)
        
        return Sneakers

def extendList(snkr):
    file = open('Sneaker.csv', 'a', encoding='utf-8')
    file.write(f'{snkr.Code};{snkr.Brand};{snkr.Type};{snkr.Colour};{snkr.Size};{snkr.Sex};{snkr.Price};{snkr.year}')
    file.close()