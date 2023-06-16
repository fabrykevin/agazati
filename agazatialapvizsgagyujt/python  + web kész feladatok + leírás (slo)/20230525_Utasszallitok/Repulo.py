class Repulo:
    def __init__(self, row) -> None:
        # típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
        # Airbus A300;1972;220-336;3;911;142000;44,84
        splitted = row.split(';')
        self.tipus = splitted[0]
        self.ev = int(splitted[1])
        self.utas = splitted[2]
        self.szemelyzet = splitted[3]
        self.utazosebesseg = int(splitted[4])
        self.felszallotomeg = int(splitted[5])
        self.fesztav = float(splitted[6].replace(',','.'))
        if '-' in self.utas:
            splitted_utas = self.utas.split('-')
            self.utas_szam = int(splitted_utas[1])
        else:
            self.utas_szam = int(self.utas)

        if '-' in self.szemelyzet:
            splitted_szemelyzet = self.szemelyzet.split('-')
            self.szemelyzet_szam = int(splitted_szemelyzet[1])
        else:
            self.szemelyzet_szam = int(self.szemelyzet)