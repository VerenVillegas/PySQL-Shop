import mysql.connector
import os 
from dotenv import load_dotenv

load_dotenv()

def db_connect():
    """
    Establishes a connection to the database.
    """
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
    """
    Closes the connection to the database.
    """
    conn.commit()
    conn.close()


def exec_proc(storedProc, args):
    """
    Executes a stored procedure from the database.

    Parameters
    -------
    storedProc : str - The name of the stored procedure.
    args : tuple - The arguments of the stored procedure.

    """
    conn = db_connect()
    if(conn):
        try:

            cursor = conn.cursor()
            if(cursor):
                if(args):
                    cursor.callproc(storedProc, args)
                else:
                    cursor.callproc(storedProc)
        except mysql.connector.Error as e:
            error_msg = str(e.msg)
            if e.errno == 1644:  # SQLSTATE '45000'
                print("Database Error:", error_msg)
            else:
                print("MySQL Error:", error_msg)
        finally:    
            db_disconnect(conn)
    else:
        print("Connection could not be established with database.")