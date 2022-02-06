import requests
import pandas as pd
import json
import redis
import subprocess
import os

if os.path.exists('/usr/bin/kubectl'):
    try:
        REDIS_HOST = subprocess.check_output("/usr/bin/kubectl get svc redis --no-headers | awk '{ print $3 }'", shell=True)
    except Exception as e:
        print(e)
        exit(1)

result = requests.get('https://learning.oreilly.com/api/v2/search/?query=python')
output = result.json()
r = redis.Redis(host=REDIS_HOST, port=6379)

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
