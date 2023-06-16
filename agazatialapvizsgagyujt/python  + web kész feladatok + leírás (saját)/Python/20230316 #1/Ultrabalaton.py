class adatok:
    def __init__(self,row) -> None:
        splitted=row.split(';')
        #Versenyzo;Rajtszam;Kategoria;Versenyido;TavSzazalek
        self.Versenyzo=splitted[0]
        self.Rajtszam=splitted[1]
        self.Kategoria=splitted[2]
        self.Versenyido=splitted[3]
        self.TavSzazalek=splitted[4]

        splittedData=self.Versenyido.split(':')
        self.ora=int(splittedData[0])
        self.perc=int(splittedData[1])
        self.masodperc=int(splittedData[2])
    def ido(self):
        return self.ora+self.perc/60+self.masodperc/3600
        
    



        
        
