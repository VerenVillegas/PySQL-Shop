import os
import json

f = open('./data/data.json')

data = json.load(f)

def print_welcome():
    """
    Prints a welcome message for the program.
    
    """
    print('%s \n' % data['welcome_message'])

def print_menu(options):
    """
    Prints the option menu for the program.

    """
    print("Menu options:")
    for option in options:
        print(f"{option['id']}. {option['text']} [Press {option['id']}]")

def clear_std_out():
    """
    Clears standard output for the program.
    
    """
    os.system('cls' if os.name == 'nt' else 'clear')