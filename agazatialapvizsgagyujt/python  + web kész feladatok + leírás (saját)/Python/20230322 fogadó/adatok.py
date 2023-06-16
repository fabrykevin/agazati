class adat:
    def __init__(self, row) -> None:
        splitedData=row.split(' ')
        self.vezeteknev=splitedData[0]
        self.utonev=splitedData[1]
        self.idopont=splitedData[2]
        self.datum=splitedData[3]
        splitted=self.datum.split('-')
        self.datum=splitted[0]
        self.ido=splitted[1]