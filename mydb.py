import mysql.connector

dataBase=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='123123',
)


cursorObject = dataBase.cursor()
cursorObject.execute("create database elderco")

print("ALL DONE!")