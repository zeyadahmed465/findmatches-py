__debugFlag = False
dbName = "d42memv3lblact"
if(__debugFlag):
    dbHost="localhost"
    dbUser="root"
    dbPassword="admin"
else:
    dbHost="ec2-54-229-68-88.eu-west-1.compute.amazonaws.com:5432"
    dbUser="wxrcljxtqhylxb"
    dbPassword="6637b00d297ea79db3e2d67e0adde0e7d844a94f05ec36ab6af982f8f2138be9"



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