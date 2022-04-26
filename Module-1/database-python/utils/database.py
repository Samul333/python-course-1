 
 
books=[]



def add_books(name,author):
    books.append({'name':name,'author':author,'read':False})
    
    

def get_all_books():
    return books

def getBook(name):
    for book in books:
        if book['name'] == name:
            return book
    return None

def delete_book(name):
    book = getBook(name)
    if book:
        books.remove(book)
        return True
    return False