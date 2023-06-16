class helsinki:
    def __init__(self, row) -> None:
        splittedData = row.split(' ')
        self.place = int(splittedData[0])
        self.numberOfMembers = int(splittedData[1])
        self.sport = splittedData[2]
        self.category = splittedData[3]

        if self.place == 1:
            self.olympicPoints = 7
        else:
            self.olympicPoints = 7 - self.place