import importlib
from constants.dialog import  USER_CHOICE
from db.db import init_database
import os

def menu():
    try:
       database =  init_database()
    except Exception as e:
        print(e)
        print('Exiting...')
        return 
    
    user_input = input(USER_CHOICE)
  
    while user_input != 'q':
        os.system('cls')
        if user_input == 'a':
           prompt_add_book(database)
        elif user_input == 'l':
            list_books(database)
            
        elif user_input == 'd':
            name = input("Enter the book name you want to delete: ")
            database.delete_book(name)
        elif user_input == 'c':
            database = init_database()
            
        else:
            print("Invalid input")
           
        
        user_input = input(USER_CHOICE)
        
        
        

def prompt_add_book(database):
    name = input("Enter the new book name: ")
    author = input("Enter the new book author: ")
    
    database.add_books(name,author)
    


def list_books(database):
    books = database.get_all_books()
    print('=========Book Listings==========')
    if not books:
        return print("No books entered into the database")
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"The book name is {book['name']} and the author is {book['author']} read :{read}")
    print('===================')       
        
if __name__ == '__main__':
    menu()