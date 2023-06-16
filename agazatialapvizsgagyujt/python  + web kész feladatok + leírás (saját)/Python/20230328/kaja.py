class Kaja:
    def __init__(self,row) -> None:
        splitted=row.split(';')
        #Fajta;Megnevezés;Ár;Rendelt mennyiség
        self.fajta=splitted[0]
        self.nev=splitted[1]
        self.ar=int(splitted[2])
        self.mennyiseg=int(splitted[3])

    def arBevetelEuroban(self):
        return self.ar*self.mennyiseg/402.5
    
    
