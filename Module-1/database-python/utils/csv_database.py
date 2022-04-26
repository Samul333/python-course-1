

BOOKS_FILE = 'books.txt'




def add_books(name,author):
    with open (BOOKS_FILE,'a') as file:
        file.write(f'{name},{author},0\n')
        




def get_all_books():
    try:
        with open(BOOKS_FILE,'r') as file:
            lines = [lines.strip().split(',') for lines in file.readlines()]
    except FileNotFoundError:
        return []    
    
    books = [
        {'name':line[0],'author':line[1],'read':int(line[2])} for line in lines
    ]
    return books
    
def mark_book_as_read(name):
    books = get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = '1'
            
    _save_all_books(books)
    
    
def _save_all_books(books):
    with open(BOOKS_FILE,'w') as file:
        for book in books:
            file.write(f'{book["name"]},{book["author"]},{book["read"]}\n')
            
            

def delete_book(name):
    books = get_all_books()
    books = [book for book in books if book['name'] != name]
    _save_all_books(books)