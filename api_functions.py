import sqlite3

#global DB_NAME = 'books.db'


def get_books():
    with sqlite3.connect('books.db') as conn:
        columns = ['id', 'title', 'isbn', 'authors', 'description']
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM books')
        book_list = []
        for book in cursor.fetchall():
            book_list.append(dict(zip(columns, book)))
        return book_list


def get_single_book(DB_NAME, id):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        for item in cursor.execute('SELECT * FROM books WHERE id = ?', [id]):
            print(item)
            return cursor.fetchone()

def add_book(title, isbn, authors, description):
    with sqlite3.connect('books.db') as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO books(title, isbn, authors, description) VALUES (?, ?, ?, ?)", [title, isbn, authors, description])
        conn.commit()
