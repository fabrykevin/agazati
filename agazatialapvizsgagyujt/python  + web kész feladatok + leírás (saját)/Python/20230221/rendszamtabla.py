def ellenorzes(rendszam): #ABC-123, AA-AA-123, 
    if len(rendszam)==7:
        if rendszam[3]== '-':
            if  rendszam[0] >='A' and rendszam[0] <='Z' and\
                rendszam[1] >='A' and rendszam[1] <='Z' and\
                rendszam[2] >='A' and rendszam[2] <='Z' and\
                rendszam[4] >='0' and rendszam[4] <='9' and\
                rendszam[5] >='0' and rendszam[5] <='9' and\
                rendszam[6] >='0' and rendszam[6] <='9':
                return True
        else: 
            return False
    elif len(rendszam)==9:
        
        return  rendszam[0] >='A' and rendszam[0] <='Z' and\
                rendszam[1] >='A' and rendszam[1] <='Z' and\
                rendszam[2] =='-'and\
                rendszam[3] >='A' and rendszam[3] <='Z' and\
                rendszam[4] >='A' and rendszam[4] <='Z' and\
                rendszam[5] =='-'and\
                rendszam[6] >='0' and rendszam[6] <='9'and\
                rendszam[7] >='0' and rendszam[7] <='9'and\
                rendszam[8] >='0' and rendszam[8] <='9'
                
        
    else:
        return False

