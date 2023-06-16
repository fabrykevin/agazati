class versenyzo:
    def __init__(self, row):
        splitted = row.split(';')
        self.nev = splitted[0]
        self.rajtszam = int(splitted[1])
        self.kategoria = splitted[2]
        self.ido = splitted[3]
        self.szazalek = int(splitted[4])


        splitted_ido=self.ido.split(':')
        self.ido_oraban=int(splitted_ido[0])+int(splitted_ido[1]/60) +int(splitted_ido[2]/3600)
