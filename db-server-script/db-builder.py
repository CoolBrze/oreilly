import requests
import pandas as pd
import json
import redis


result = requests.get('https://learning.oreilly.com/api/v2/search/?query=python')
output = result.json()
r = redis.Redis()

def build_table():
    book_json = {"books":[]}
    for book in output['results']:
        try:
            book_dict = {'title': book['title'], 'isbn': book["isbn"], 'authors': ", ".join(book['authors']), 'description': book['description']}
        except KeyError:
            pass
        book_json["books"].append(book_dict)
    redis_json = json.dumps(book_json["books"])
    r.set('books', redis_json)

build_table()
