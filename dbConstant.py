__debugFlag = False

def getIsDebug():
    global __debugFlag
    
    return __debugFlag

if(__debugFlag):
    dbName = "findMatches"
    dbHost="localhost"
    dbUser="root"
    dbPassword="admin"
else:
    dbName = "dd2qgtr65ivri"
    dbHost="ec2-52-49-23-139.eu-west-1.compute.amazonaws.com"
    dbUser="ogocxhnososutv"
    dbPassword="0290e224773b8a1c51bc76158f2a776c9ef99926447e85ba0dd6925d89fc081a"



mysqlCreateTable = '''
Create Table IF NOT EXISTS scores (
    id INTEGER NOT NULL AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    level INTEGER DEFAULT 1,
    time DECIMAL NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,

    CONSTRAINT unique_name_level unique(name, level),
    PRIMARY KEY (id)
)
'''

postsqlCreateTable = '''
Create Table IF NOT EXISTS scores (
    id serial  NOT NULL,
    name VARCHAR(255) NOT NULL,
    level INTEGER DEFAULT 1,
    time DECIMAL NOT NULL,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    UNIQUE(name, level),
    PRIMARY KEY (id)
)
'''