from flask import Flask, jsonify, request
import api_functions
import json

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_all_books():
    books = api_functions.get_books()
    return jsonify(books)

@app.route('/books/v1/GetField', methods=["GET"])
def get_books_by_search():
    query = request.query_string.decode()
    param = query.split("=",1)[1]
    books = api_functions.get_single_type(param)
    return jsonify({param: books})

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