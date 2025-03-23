import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

database = mysql.connector.connect(
    host=os.getenv('DB_HOST'),
    user=os.getenv('DB_USER'),
    passwd=os.getenv('DB_PASSWORD'),
    auth_plugin='mysql_native_password'
)

#prepare a cursor object
cursor = database.cursor()

#create a database
cursor.execute("CREATE DATABASE dcrm")

print("Database created successfully")