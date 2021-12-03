import requests
import constants as c
class Score:
    def __init__(self, name:str, time:float, level:int) -> None:
        self.name = name
        self.time = time
        self.level = level
        
    def __str__(self):
        return "Score(Name: " + self.name+ " - Time: " + str(self.time) + " - Level: "+ str(self.level)+")" +"\n"
    
    def __repr__(self):
        return self.__str__()

    
    
    def storeScore(self):
        return requests.post(c.url,json={"name":self.name, "time":self.time, "level":self.level})
        
    
    @staticmethod
    def getLevel(level = 1):
        response = requests.get(c.url+"/"+str(level))
        return (response.json())
        
        
    