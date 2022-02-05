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
    print(param_dict)
    print(param_list)
    return param_list


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

