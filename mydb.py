import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="Vasu@2004",
    auth_plugin='mysql_native_password'
)

#prepare a cursor object
cursor = database.cursor()

#create a database
cursor.execute("CREATE DATABASE dcrm")

print("Database created successfully")