class Fogadasi_fordulo:
    def __init__(self, sor: str):
        splittedData = sor.strip().split(';')
        self.ev = int(splittedData[0])
        self.het = int(splittedData[1])
        self.fordulo = int(splittedData[2])
        self.t13p1 = int(splittedData[3])
        self.ny13p1 = splittedData[4]
        self.eredmenyek = splittedData[5]

    