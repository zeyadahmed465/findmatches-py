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
    except Exception as e:
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
    if(dbConstant.getIsDebug()):
        sql = '''INSERT INTO scores(name, time, level) VALUES (%s,%s, %s)
            ON DUPLICATE KEY UPDATE name = %s, time = %s, level =%s'''
        val = (name, time, level)*2
    else:
        sql = '''
            INSERT INTO scores (name, time, level) 
            VALUES (%s,%s, %s)
            ON CONFLICT (name, level) DO UPDATE 
            SET time = EXCLUDED.time
            '''
        val = (name, time, level)
    try:
        initDB.cursor.execute(sql, val)
        initDB.connection.commit()
        return "Stored"
    except initDB.Error as e:
        return e.args

def getLevel(level = 1):
    try:
        sql = "SELECT name,time,level FROM scores WHERE level = %s ORDER BY time"
        initDB.cursor.execute(sql, (level, ))
        return initDB.cursor.fetchall()
    except initDB.Error as e:
        return e.args
        
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
    