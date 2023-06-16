from data import telepulesek
def legkisebb():
    minimum = 99999
    for telepules in telepulesek :
        darabolt = int(telepules.split(';').replace())
        if int(darabolt[3]) < minimum:
            minimum = int(darabolt[3])
    return darabolt[0]


def legkisebb():
minimum =0
    for telepules in telepulesek :
        darabolt = int(telepules.split(';').replace())
        if darabolt[4] < maximum:
            maximum=darabolt[4]
    return maximum




