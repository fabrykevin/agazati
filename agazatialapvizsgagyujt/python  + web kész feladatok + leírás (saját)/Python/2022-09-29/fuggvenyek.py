from cars import cars

def searchPlate(plate):
    for car in cars:
        splitteData=car.split(';')
        if splitteData[0].upper() ==plate.upper():
            return True
    return False

def totalPrice():
    sum=0
    for car in cars:
        splitteData=car.split(';')
        sum+= int(splitteData[4])
        
    return sum

def averageAge():
    sum=0
    for car in cars:
        splitteData=car.split(';')
        sum+=2022-int(splitteData[2])
    return sum /len(cars)

def countBrand(brand):
            count=0
            for car in cars:
                splitteData=car.split(';')
                if splitteData[1].upper()== brand.upper():
                    count+=1
            return count
def highestPower():

            best=0
            for car in cars:
                splitteData=car.split(';')
                currentPower= int(splitteData[7])
                if currentPower>best:
                    best= currentPower
            return best

def lowestConsumption():
            lowest=9999
            for car in cars:
                splitteData=car.split(';')
                currentcons= float(splitteData[8])
                if currentcons>lowest:
                    best= currentcons
            return lowest
                
            
        