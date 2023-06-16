


def duration(row:str):
    splittedData= row.split(';')
    d=splittedData[3]
    timeData =d.split(':')
    miunte= int(timeData[0])
    seconds=int(timeData[1])
    return miunte*60+seconds


def publishedYear(row):
    splittedData= row.split(';')
    return int(splittedData[4])

def category(row):
    splittedData= row.split(';')
    return splittedData[5]
def performer(row):
    splittedData= row.split(';')
    return splittedData[1]
    
