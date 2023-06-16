from menu import *
from functions import *


names=[]
def load():
    file = open('people.csv', 'r', encoding='utf-8')
    for row in file:
        names.append(row.strip())
    
    file.close


def showall():
        print('Összes felhasználó')
        for name in names:
            print(name, end=',')
        print()
def search(needle):
    results=[]
    for name in names:
        if needle.upper() in name.upper():
            results.append(name)
    return results

def searchWithIndex(needle):
    results=[]
    for index in range(len(names)):
        if needle.upper() in names[index].upper():
            results.append(index)
    return results

def new(name):
    names.append(name)
    file = open('people.csv', 'a', encoding='utf-8')
    file.write(name+ '\n')    
    file.close
def delete(name):
    if name in names:
        names.remove(name)
        writeNamesToFile()
def update(old, new):
    names.remove(old)
    names.append(new)
    writeNamesToFile()


def updateByIndex(index, new):
    names.pop(index)
    names.append(new)
    writeNamesToFile()


def writeNamesToFile():
    file = open('people.csv', 'w', encoding='utf-8')
    for name in names:
        file.write(name+' \n')
    file.close()


