class Celeb:
    name = ''
    job = ''
    nationality = ''
    
    def prefix(self):
        if self.nationality.lower() == 'a':
            return 'Ms.'
        return 'Frau'