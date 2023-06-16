class adat:
    def __init__(self, row:str) -> None:
        splittedData=row.split(';')
        #hazai;idegen;hazai_pont;idegen_pont;helyszín;időpont
        self.hazai=splittedData[0]
        self.idegen=splittedData[1]
        self.hazai_pont=int(splittedData[2])
        self.idegen_pont=int(splittedData[3])
        self.helyszín=splittedData[4]
        self.időpont=splittedData[5]
        

        