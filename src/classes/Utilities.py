import os
from src.classes import Database

def print_message(message):
    """
    Prints a welcome message for the program.
    
    """
    print('%s \n' % message)

def print_menu(options):
    """
    Prints the option menu for the program.

    """

    print("Menu options:")
    for option in options:
        print(f"{option['id']}. {option['text']} [Press {option['id']}, then press 'Enter']")

def manage_menu(options):
    dict_func = {}
    dict_sp = {}
    exit_num = len(options)
    for option in options:
        dict_func[option['id']] = option['func']
        dict_sp[option['id']] = option['sp']
    user_choice = input()
    clear_std_out()
    if(user_choice in dict_func and user_choice in dict_sp):
        if(int(user_choice) == exit_num):
            exit()
        else:
            if(dict_func[user_choice] is not "None"):
                f = getattr(Database, dict_func[user_choice])
                args = f()
                val = Database.exec_proc(dict_sp[user_choice], args)
                for row in val:
                    print(row.fetchall())
    else:
        print("Please select one of the available options. \n")
        print_menu(options)
        manage_menu(options)


def clear_std_out():
    """
    Clears standard output for the program.
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')