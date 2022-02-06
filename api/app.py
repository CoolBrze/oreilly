from flask import Flask, jsonify, request
import api_functions
import json

app = Flask(__name__)

@app.route('/health', methods=["GET"])
def get_health():
    return jsonify({"success": True})

@app.route('/books', methods=["GET"])
def get_all_books():
    books = api_functions.get_books()
    return jsonify(books)

@app.route('/books/v1/GetField', methods=["GET"])
def get_books_by_field():
    query = request.query_string.decode()
    param = query.split("=",1)[1]
    books = api_functions.get_single_type(param)
    print(param)
    print(books)
    if books and param:
        return jsonify({param: books})
    else:
        return jsonify({'EmptySet': f"Unable to parse by field, please try 'title', 'isbn', 'authors', or 'description'"})

@app.route('/books/v1/GetByTitle', methods=["GET"])
def get_title_book():
    query = request.query_string.decode()
    try:
        param = query.split("=", 1)[1]
    except IndexError:
        return jsonify({'No_query_set': 'No query was found, please query ISBNs by \'?query=\''})
    if param:
        pass
    else:
        return jsonify({'No_query_set': 'No query was found, please query titles by \'?query=<parameter>\''})
    books = api_functions.get_by_title(param)
    if books:
        return jsonify({'Found_titles': books})
    else:
        return jsonify({'EmptySet': 'No books found by that title'})

@app.route('/books/v1/GetByISBN', methods=["GET"])
def get_isbn_book():
    query = request.query_string.decode()
    try:
        param = query.split("=",1)[1]
    except IndexError:
        return jsonify({'No_query_set': 'No query was found, please query ISBNs by \'?query=\''})
    if param:
        pass
    else:
        return jsonify({'No_query_set': 'No query was found, please query ISBNs by \'?query=<parameter>\''})
    books = api_functions.get_by_isbn(param)
    if books:
        return jsonify({'Found_books': books})
    else:
        return jsonify({'EmptySet': 'No books found by that ISBN'})

@app.route('/books/v1/AddBook', methods=["POST"])
def add_a_book():
    try:
        books = request.get_json()
        authors = books["authors"]
        description = books["description"]
        isbn = books["isbn"]
        title = books["title"]
    except Exception as e:
        return f"[success: False] There was an error within your request body, check your syntax for {e}\n"
    api_functions.add_book(authors=authors, description=description, isbn=isbn, title=title)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=False)
