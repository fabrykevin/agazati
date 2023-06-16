class adat:
    def __init__(self, row) -> None:
        splittedData=row.split('\t')
        self.nev=splittedData[0]
        self.honap=int(splittedData[1])
        self.nap=int(splittedData[2])
        self.szam=int(splittedData[3])
        self.hossza=int(splittedData[4])
        self.cim=splittedData[5]
        self.eszkozok=splittedData[6]