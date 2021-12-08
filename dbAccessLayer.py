import initDB
from initDB import dbConstant

if(dbConstant.getIsDebug()):
    initDB.cursor.execute("USE {}".format(dbConstant.dbName))
    initDB.cursor.execute(dbConstant.mysqlCreateTable)

else:
    initDB.cursor.execute(dbConstant.postsqlCreateTable)

def tryIfConnected(funToLoad):
    try:
        if initDB.connection.is_connected():
            funToLoad
        else:
            print("ERROR")
            exit()
    except initDB.Error as e:
        print(e)

def buildQuery(query):
    try:
        initDB.cursor.execute(query)
        initDB.connection.commit()
    except initDB.Error as e:
        print(e)

def dropTable(table):
    try:
        initDB.cursor.execute("DROP TABLE {}".format(table))
        initDB.connection.commit()
    except initDB.Error as e:
        pass


def insertIntoScore(name,time, level):
    #sql = "REPLACE INTO score(name, time) VALUES (%s,%s)"
    sql = '''INSERT INTO scores(name, time, level) VALUES (%s,%s, %s)
    ON DUPLICATE KEY UPDATE name = %s, time = %s, level =%s'''
    val = (name, time, level)*2
    try:
        initDB.cursor.execute(sql, val)
        initDB.connection.commit()
    except initDB.Error as e:
        return e

def getLevel(level = 1):
    sql = "SELECT name,time,level FROM scores WHERE level = %s ORDER BY time"
    initDB.cursor.execute(sql, (level,))
    return initDB.cursor.fetchall()
        
def seeder(records = 1):
    import random
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxwy"
    #letters = random.shuffle(letters)
    for _ in range(records):
        name = "".join(random.choices(letters, k=5))
        values = [(name, random.randrange(1, 200), level) for level in range(1, 4)]
        sql = '''INSERT INTO scores(name, time, level) VALUES (%s,%s, %s)'''
        initDB.cursor.executemany(sql, values)
        initDB.connection.commit()
    

