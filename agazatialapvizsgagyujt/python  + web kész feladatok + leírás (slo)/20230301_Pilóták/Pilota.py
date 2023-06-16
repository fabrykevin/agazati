# név;születési_dátum;nemzetiség;rajtszám
# Lewis Hamilton;1985.01.07;brit;44

class Pilota:

    def __init__(self, row) -> None:
        splittedData = row.split(';')
        self.nev = splittedData[0]
        self.datum = splittedData[1]
        self.nemzetiseg = splittedData[2]
        self.rajtszam = splittedData[3]
        splittedDatum = self.datum.split('.')
        self.ev = int(splittedDatum[0])