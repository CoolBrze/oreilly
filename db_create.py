import os
import requests
import pandas as pd
from sqlalchemy import create_engine
import sqlite3

DB_NAME = 'books.db'
result = requests.get('https://learning.oreilly.com/api/v2/search/?query=python')
output = result.json()

def build_table():
    book_json = {"books":[]}
    for book in output['results']:
        try:
            book_dict = {'title': book['title'], 'isbn': book["isbn"], 'authors': ", ".join(book['authors']), 'description': book['description']}
        except KeyError:
            pass
        book_json["books"].append(book_dict)

    engine = create_engine('sqlite:///books.db')
    df = pd.DataFrame(book_json['books'])

    with sqlite3.connect('books.db') as conn:
        cursor = conn.cursor()
        cursor.execute( """CREATE TABLE IF NOT EXISTS books(
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                title TEXT NOT NULL,
                                isbn TEXT NOT NULL,
                                authors TEXT NOT NULL,
                                description TEXT NOT NULL 
                        )"""
                        )

    try:
        df.to_sql('books', con=engine, if_exists='append', index_label='id')
    except Exception as e:
        print(e)

