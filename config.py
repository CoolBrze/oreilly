from app import app
#rom flaskext.mysql import MYSQL
import os
import requests
import pandas as pd
from sqlalchemy import create_engine

result = requests.get('https://learning.oreilly.com/api/v2/search/?query=python')
output = result.json()

book_json = {"books":[]}
for book in output['results']:
    try:
        book_dict = {'title': book['title'], 'isbn': book["isbn"], 'authors': ", ".join(book['authors']), 'description': book['description']}
    except KeyError:
        pass
    book_json["books"].append(book_dict)

engine = create_engine('sqlite:///books.db')
df = pd.DataFrame(book_json['books'])
try:
    if os.path.exists('books.db'):
        os.remove('books.db')
    df.to_sql('books', con=engine)
except Exception as e:
    print(e)

mysql = MYSQL()
mysql.init_app(app)