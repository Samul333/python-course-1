
import json

BOOKS_FILE = 'books.json'




def add_books(name,author):
    books = get_all_books()
    books.append({'name':name,'author':author,'read':False})
    _save_all_books(books)
        




def get_all_books():
    try:
        with open(BOOKS_FILE,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []    
    
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
            
    _save_all_books(books)
    
    
def _save_all_books(books):
    with open(BOOKS_FILE,'w') as file:
        json.dump(books,file)
            
            

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)