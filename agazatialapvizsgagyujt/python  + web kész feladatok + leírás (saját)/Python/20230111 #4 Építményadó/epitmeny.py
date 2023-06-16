class epitmeny:
    def __init__(self, sor:str) -> None:
         #79028 Aradi 15 C 213
         splitted=sor.split(' ')
         self.adoszam=splitted[0]
         self.utca=splitted[1]
         self.hazszam=splitted[2]
         self.tipus=splitted[3]
         self.terulet=int(splitted[4])
