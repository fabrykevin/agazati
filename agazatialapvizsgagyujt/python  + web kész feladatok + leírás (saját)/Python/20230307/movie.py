class Movie:
    def __init__(self,sor) -> None:
    #id	title	tags	director	stars	length	country  releaseyear
    #1	A remény rabjai	Drama	Frank Darabont	Tim Robbins, Morgan Freeman, Bob Gunton	2 hours 22 minutes	United States	1994
        splitteddata=sor.strip().split('\t')
        self.id=splitteddata[0]
        self.title=splitteddata[1]
        self.tags=splitteddata[2]
        self.director=splitteddata[3]
        self.stars=splitteddata[4]
        self.length=splitteddata[5]
        self.country=splitteddata[6]
        self.releaseyear=int(splitteddata[7]) 

    def lengthInMinutes(self):
        #2 hours 22 minutes
        #2 hours
        #45 minutes
        splittedData=self.length.split(' ')
        hour=int(splittedData[0])
        if len(splittedData)==2:
            if splittedData[1]=='hours' or splittedData[1]=='hour':    
                return hour*60
            else:
                return hour

        minute=int(splittedData[2])
        return hour*60+minute

        
