class price:
    def __init__(self, row) -> None:
        splitted=row.split(';')
        self.date=splitted[0]
        self.petrol=int(splitted[1])
        self.diesel=int(splitted[2])
        self.difference=abs(self.petrol-self.diesel) #abszolútérték(mert nem tudjuk melyik a nagyobb)
        splittedDate=self.date.split('.')
        self.year=int(splittedDate[0])
        self.month=int(splittedDate[1])
        self.day=int(splittedDate[2])

        if self.year % 4==0 and self.day==24 and self.month==2:
            self.leapDay=True
        else: 
            self.leapDay=False
