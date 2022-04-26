from constants.dialog import DB_CHOICE
import importlib

def init_database():
    database = None
    db_choice = input(DB_CHOICE)
    
    if db_choice == 'a':
        database = importlib.import_module('utils.database')
    elif db_choice == 'b':
        database = importlib.import_module('utils.csv_database')
    elif db_choice == 'c':
        database = importlib.import_module('utils.json_database')
    elif db_choice == 'd':
        database = importlib.import_module('utils.sql_database')
    else:
        raise Exception('Invalid choice')
    print(database)
    return database
