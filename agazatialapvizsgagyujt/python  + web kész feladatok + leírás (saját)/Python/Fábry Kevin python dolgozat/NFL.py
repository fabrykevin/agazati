
class NFLadatok:
    def __init__(self, row) -> None:
        splitted=row.split(';')
        #Nev;Yardok;Kiserletek;Sikeres;TD passzok;Eladott;Iranyitomutato;Egyetem
        self.nev=splitted[0]
        self.yardok=int(splitted[1])
        self.kiserletek=int(splitted[2])
        self.sikeres=int(splitted[3])
        self.TDpasszok=int(splitted[4])
        self.eladott=int(splitted[5])
        self.iranyitomutato=float(splitted[6].replace(',', '.'))
        self.egyetem=splitted[7]
        
    def yard(self):
            return round(self.yardok*0.9144)
      
        