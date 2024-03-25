from src.classes import Utilities
import json

f = open('./data/data.json')

data = json.load(f)

Utilities.clear_std_out()
Utilities.print_message(data["welcome_message"])
Utilities.print_menu(data["main_menu_options"])
Utilities.manage_menu(data["main_menu_options"])







