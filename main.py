from src.classes import Database
from src.classes import Utilities


Utilities.clear_std_out()
Utilities.print_welcome()



args = ("Tree", -45, 2)
Database.exec_proc("add_new_product", args)







