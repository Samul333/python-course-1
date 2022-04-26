import sqlite3
from venv import create






def create_book_table():
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    
    connection.commit()
    connection.close()
    
    
    
def add_books(name,author):
    create_book_table()
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    print(name,author)
    try:
        cursor.execute('INSERT INTO books VALUES(?,?,0)',(name,author))
        connection.commit()
    except sqlite3.IntegrityError:
        print('Book already exists')
    except Exception as e:
        print(e)
    finally:

        connection.close()
    
    
def get_all_books():
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    books = [{'name':row[0],'author':row[1], 'read':row[2]} for row in cursor.fetchall() ]
    connection.close()
    
    return books

def mark_book_as_read(name):
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    
    cursor.execute('UPDATE books SET read=1 WHERE name=?',(name,))
    
    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('database.db') 
    cursor = connection.cursor()
    
    cursor.execute('DELETE FORM books WHERE names = ?',(name,))
    
    connection.commit()
    connection.close()      