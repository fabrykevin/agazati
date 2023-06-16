class  adat:
    def __init__(self, row:str) -> None:
        splitted=row.split(';')
        self.nev=splitted[0]
        self.születési_dátum=splitted[1]
        self.nemzetiség=splitted[2]
        self.rajtszám=splitted[3]
        splittedDatum=self.datum.split()
        



