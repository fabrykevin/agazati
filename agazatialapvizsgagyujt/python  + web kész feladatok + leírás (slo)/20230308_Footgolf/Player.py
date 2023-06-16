class Player:
    def __init__(self, row) -> None:
        splitted = row.strip().split(';')
        self.name = splitted[0]
        self.category = splitted[1]
        self.club = splitted[2]
        # self.point1 = int(splitted[3])
        self.points = []
        for i in range(3,len(splitted)):
            self.points.append(int(splitted[i]))

        # for item in splitted[3:]:
        #     self.points.append(int(item))