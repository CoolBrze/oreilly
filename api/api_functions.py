import redis
import json
from flask import jsonify


r = redis.Redis(host='redis', port=6379)

def get_books():
        redis_data = r.get('books')
        if redis_data is None:
            return {'EmptySet': 'No data for books exists'}
        else:
            pulled_books = json.loads(redis_data)
            return pulled_books




def get_single_type(param):
    redis_data = r.get('books')
    if redis_data is None:
        return {'EmptySet': 'No data for books exists'}
    param_list = []
    N = 1
    if isinstance(redis_data, bytes):
        redis_data = json.loads(redis_data)
    print(redis_data)
    for item in redis_data:
        if item == {}:
            continue
        param_dict = {N : item[param]}
        param_list.append(param_dict)
        N += 1
    return param_list

def get_by_title(param):
    redis_data = r.get('books')
    if redis_data is None:
        return {'EmptySet': 'No data for books exists'}
    found_titles = []
    if isinstance(redis_data, bytes):
        redis_data = json.loads(redis_data)
    for entry in redis_data:
        if entry == {}:
            continue
        listed_title = entry['title'].split()
        concat_title = "+".join(listed_title)
        if param in concat_title.lower():
            found_titles.append(entry)
        else:
            pass
    return found_titles

def get_by_isbn(param):
    redis_data = r.get('books')
    if redis_data is None:
        return {'EmptySet': 'No data for books exists'}
    if isinstance(redis_data, bytes):
        redis_data = json.loads(redis_data)
    found_titles = []
    for entry in redis_data:
        if entry == {}:
            continue
        if param in entry['isbn']:
            found_titles.append(entry)
        else:
            pass
    return found_titles

def add_book(title, isbn, authors, description):
    redis_data = r.get('books')
    if redis_data is None:
        redis_data = [{}]
    added_book = {
        "title": title,
        "isbn": isbn,
        "authors": authors,
        "description": description
    }
    if isinstance(redis_data, bytes):
        redis_data = json.loads(redis_data)
    redis_data.append(added_book)
    print(type(redis_data))
    r.set('books', json.dumps(redis_data))

