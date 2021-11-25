import mysql.connector
from mysql.connector import Error
import dbConstant

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
    