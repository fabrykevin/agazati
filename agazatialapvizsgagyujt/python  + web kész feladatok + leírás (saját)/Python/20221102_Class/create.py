from Result import Result

def addResult():
    print('Új adatok megadása: ')
    res=Result()
    res.name=input('Tanuló neve')
    res.module=input('Modul')
    res.time=input('Idő')
    res.resultinput=int(input('Eredmény:'))
    return res
