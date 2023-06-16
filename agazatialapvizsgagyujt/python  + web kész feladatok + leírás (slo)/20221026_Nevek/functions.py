names = []

def load():
    file = open('people.csv', 'r', encoding='utf-8')

    for row in file:
        names.append(row.strip())

    file.close()

def showAll():
    print('Összes felhasználó')
    for name in names:
        print(name, end=', ')
    print()

def search(needle):
    results = []
    for name in names:
        if needle.upper() in name.upper():
            results.append(name)
    return results

def new(name):
    names.append(name)

    file = open('people.csv', 'a', encoding='utf-8');
    file.write(name + '\n')
    file.close()

def delete(name):
    if name in names:
        names.remove(name)
    writeNamestoFile()

def update(old, new):
    names.remove(old)
    names.append(new)
    writeNamestoFile()

def writeNamestoFile():
    file = open('people.csv', 'w', encoding='utf-8');
    for name in names:
        file.write(name + '\n')
    file.close()