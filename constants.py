__isDebug = False

if __isDebug:
    url = "http://localhost:8000"
else:
    url = "https://find-matches.herokuapp.com"
    
__level = 0
def getLevel():
    global __level
    return __level

def setLevel(l):
    global __level
    __level = l
