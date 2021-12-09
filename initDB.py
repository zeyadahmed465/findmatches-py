import dbConstant

if(dbConstant.getIsDebug()):
    import mysql.connector
    from mysql.connector import Error
else:
    import psycopg2
    from psycopg2 import Error



if(not dbConstant.getIsDebug()):
    try:
        connection = psycopg2.connect(
        host=dbConstant.dbHost,
        user=dbConstant.dbUser,
        password=dbConstant.dbPassword,
        dbname = dbConstant.dbName)

        cursor = connection.cursor()
    except Exception as e:
        connection = psycopg2.connect(
        host=dbConstant.dbHost,
        user=dbConstant.dbUser,
        password=dbConstant.dbPassword)
        cursor = connection.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {dbConstant.dbName}")
        connection.commit()
        
else:
    try:
        connection = mysql.connector.connect(
        host=dbConstant.dbHost,
        user=dbConstant.dbUser,
        password=dbConstant.dbPassword,
        database = dbConstant.dbName)

        if connection.is_connected():
            cursor = connection.cursor()
    except Error as e:
        connection = mysql.connector.connect(
        host=dbConstant.dbHost,
        user=dbConstant.dbUser,
        password=dbConstant.dbPassword)
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS findmatches")
        connection.commit()
        