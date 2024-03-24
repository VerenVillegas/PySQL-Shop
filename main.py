import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

conn = mysql.connector.connect(
    host = "localhost",
    user = os.getenv("DATABASE_USER"),
    password = os.getenv("DATABASE_PASSWORD"),
    database = os.getenv("DATABASE_NAME")
)

cursor = conn.cursor()

args = ("Bundaberg Ginger Beer", 12.99, 30) 

cursor.callproc("add_new_product", args)


conn.commit()
conn.close()

