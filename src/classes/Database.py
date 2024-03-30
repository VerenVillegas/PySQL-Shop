import mysql.connector
import os
import re
from dotenv import load_dotenv
from src.classes import Utilities

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
            val = None
            cursor = conn.cursor()
            if(cursor):
                if(args):
                    cursor.callproc(storedProc, args)
                else:
                    cursor.callproc(storedProc)
                val = cursor.stored_results()
                return val
            
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


def validate_input(prompt, regex):
    """
    Validates a user input against a regular expression.

    Parameters
    ----------
    prompt: str - The prompt for the user's input, which is printed to the terminal.
    regex: regexp - The regular expression to match against the user's input.
    """
    while True:
        user_input = input(prompt + ": ")
        if re.match(regex, user_input):
            return user_input
        else:
            Utilities.clear_std_out()
            print(f"Invalid {prompt.lower()}. Please try again.\n")

def add_product():
    """
    Guides the user through a series of prompts to create a new product then returns all of the product details.
    """
    name_regex = r"^(?=.*[a-zA-Z])[\w'-]+(?:[\s_-][\w'-]+)*$"
    price_regex = r'^\d+(?:\.\d{1,2})?$'
    quantity_regex = r'^\d+$'
    product_name = validate_input("Product name", name_regex)
    product_price = validate_input("Product price ($)", price_regex)
    product_quantity = validate_input("Product quantity (units)", quantity_regex)
    return (product_name, product_price, product_quantity)

def find_product():
    name_regex = r"^(?=.*[a-zA-Z])[\w'-]+(?:[\s_-][\w'-]+)*$"
    barcode_regex = r'^\d+$'
    product_name = validate_input("Product name", name_regex )
    product_barcode = validate_input("Product barcode", barcode_regex)
    return (product_barcode, product_name)