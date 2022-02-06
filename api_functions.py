import redis
import json


r = redis.Redis()

def get_books():
        redis_data = r.get('books')
        pulled_books = json.loads(redis_data)
        return pulled_books


def get_single_type(param):
    redis_data = json.loads(r.get('books'))
    param_list = []
    N = 1
    for item in redis_data:
        param_dict = {N : item[param]}
        param_list.append(param_dict)
        N += 1
    return param_list

def get_by_title(param):
    redis_data = json.loads(r.get('books'))
    found_titles = []
    for entry in redis_data:
        listed_title = entry['title'].split()
        concat_title = "+".join(listed_title)
        if param in concat_title.lower():
            found_titles.append(entry)
        else:
            pass
    return found_titles

def get_by_isbn(param):
    redis_data = json.loads(r.get('books'))
    found_titles = []
    for entry in redis_data:
        if param in entry['isbn']:
            found_titles.append(entry)
        else:
            pass
    return found_titles

def add_book(title, isbn, authors, description):
    redis_data = json.loads(r.get('books'))
    added_book = {
        "title": title,
        "isbn": isbn,
        "authors": authors,
        "description": description
    }
    redis_data.append(added_book)
    r.set('books', json.dumps(redis_data))

