class Auto:
    def __init__(self,row) -> None:
        #Típus;Márka;Évjárat;Ár;Üzemanyag;Színe;Jutalék%
        splittedData=row.strip().split(';')
        self.tipus=splittedData[0]
        self.marka=splittedData[1]
        self.evjarat=int(splittedData[2])
        self.ar=int(splittedData[3])
        self.uzemanyag=splittedData[4]
        self.szin=splittedData[5]
        self.jutalek=float(splittedData[6].replace(',','.'))