from Result import Result

def loadData():
    
    results=[]
    file=open('ecdl.csv', 'r', encoding='utf-8')

    file.readline()
    for row in file:
        #egy sorból akarunk egy Result-ot csinálni
        
        splitted=row.split(';')
        res=Result()
        res.name=splitted[0]
        res.module=splitted[1]
        res.time=splitted[2]
        res.result=int(splitted[3])


        results.append(res)

    file.close()
    return results

def saveResult(res):
    file=open('ecdl.csv', 'a' , encoding='utf-8') 
    file.write(f'{res.name}; {res.module};{res.time}; {res.result}\n')


    file.close()