import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

def db_connect():
    conn = None
    try:
        conn = mysql.connector.connect(
            host = os.getenv("DATABASE_HOST"),
            user = os.getenv("DATABASE_USER"),
            password = os.getenv("DATABASE_PASSWORD"),
            database = os.getenv("DATABASE_NAME")
        )
    except:
        raise RuntimeError("Could not connect to database.")
    finally:
        return conn

def db_disconnect(conn):
    conn.commit()
    conn.close()

def exec_proc(storedProc, args):
    conn = db_connect()
    if(conn):
        cursor = conn.cursor()
        if(cursor):
            if(args):
                cursor.callproc(storedProc, args)
            else:
                cursor.callproc(storedProc)
        db_disconnect(conn)
    else:
        print("Connection could not be established with database.")