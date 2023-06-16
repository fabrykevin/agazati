class  adat:
    def __init__(self, row:str) -> None:
        splitted=row.split(';')
        self.helyezes=splitted[0]
        self.Nev=splitted[1]
        self.Orszag=splitted[2]
        self.Nyeremeny=int(splitted[3])
