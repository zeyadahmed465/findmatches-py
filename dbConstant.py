__debugFlag = True
dbName = "findMatches"
if(__debugFlag):
    dbHost="localhost"
    dbUser="root"
    dbPassword="admin"
else:
    dbHost="localhost"
    dbUser="yourusername"
    dbPassword="yourpassword"



sqlCreateTable = '''
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