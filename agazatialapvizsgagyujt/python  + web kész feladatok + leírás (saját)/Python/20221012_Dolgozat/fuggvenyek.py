from varosok import városok


def varosokszama():
    return len(városok)



def Legnepesebbvaros():
    maximum = 0
    for varos in városok:
        splittedData = varos.split(';')
        jelenlegi = int(splittedData[2])
        if jelenlegi > 10000000:
            return maximum
            

        

def lakosokszama():
    sum = 0 
    for varos in városok:
        splittedData = varos.split(';')
        sum += int(splittedData[2])
        return sum






def lakossag(varos):
    maximum=0
    for varos in városok:
        splittedData=varos.split(';')
        jelenlegi=int(splittedData[2])
        if jelenlegi> splittedData:
            maximum=splittedData
    return maximum[0:2]  






def Varos(varos):
    for varos in városok:
        splittedData=varos.split(';')
        if splittedData[0]== varos:
            return True
    return False






    
    



