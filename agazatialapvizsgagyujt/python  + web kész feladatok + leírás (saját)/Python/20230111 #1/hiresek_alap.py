class Celeb:
    name = ''
    job = ''
    nationality = ''
    
    def nemzetiseg(self):
        if self.nationality.lower()=='a':
            return 'Ms'
        elif self.nationality.lower()=='n': 
            return 'Frau'
        return False
