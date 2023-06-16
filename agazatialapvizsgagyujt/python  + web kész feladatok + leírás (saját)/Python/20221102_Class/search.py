

def searchByName(results,name):
    for index,item in enumerate(results):
        if item.name==name:
            return index
    return False
def searchByName2(results,name):
    for item in results:
        if item.name==name:
            return item 
    return False

def searchUnder(results, limit):
    failedStudents=[]
    for item in results:
        if item.result< limit:
            failedStudents.append(item)
    return failedStudents 