class helsinki:
    def __init__(self, row) -> None:
        splitted=row.split(' ')
        self.helyezes=int(splitted[0])
        self.sportolokSzama=splitted[1]
        self.sportag=splitted[2]
        self.versenyszam=splitted[3]
        
        if self.helyezes==1:
             self.olympicPoints=7
        elif self.helyezes==2:
             self.olympicPoints=5
        elif self.helyezes==3:
             self.olympicPoints=4
        elif self.helyezes==4:
             self.olympicPoints=3
        elif self.helyezes==5:
             self.olympicPoints=2
        elif self.helyezes==6:
             self.olympicPoints=1

    