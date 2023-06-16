from data import results, name

def searchByName():
    n= input('Kérem a keresett nevet:')
    for row in results:
        splittedData=row.plit(';')
        if splittedData[0]==n:
            return True

    return False


