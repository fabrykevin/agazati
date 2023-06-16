class adatok:
    def __init__(self, row) -> None:
        splitted=row.split(';')
        #Albert Laszlo;Felnott ferfi;HOLE HUNTERS;0;0;10;10;0;0;0;10
        self.nev=splitted[0]
        self.kategoria=splitted[1]
        self.egyesulet=splitted[2]
        self.pontok=[]
        for i in range(3, len(splitted)):
            self.pontok.append(int(splitted[i]))

        # for item in splitted[3:]:
        #     self.pontok.append(int(item))


    def totalPoints(self):
        self.pontok.sort()
        sum=0
        for item in self.pontok[2:]:
            sum+=item
        if self.pontok[0]!=0:
            sum+=10
        if self.pontok[1]!=0:
            sum+=10
        return sum