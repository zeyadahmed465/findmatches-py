import dbAccessLayer

class Score:
    def __init__(self, name:str, time:float, level:int) -> None:
        self.name = name
        self.time = time
        self.level = level
        
    def __str__(self):
        return "Score(Name: " + self.name+ " - Time: " + str(self.time) + " - Level: "+ str(self.level)+")" +"\n"
    
    def __repr__(self):
        return self.__str__()

    
    
    def storeScore(data):
        return dbAccessLayer.insertIntoScore(**data)
        
    
    @staticmethod
    def getLevel(level = 1):
        return [Score(*d) for d in dbAccessLayer.getLevel(level)]
        
    


