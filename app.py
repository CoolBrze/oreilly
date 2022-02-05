from flask import Flask, jsonify, request
import api_functions
from db_create import build_table
import json

app = Flask(__name__)

@app.route('/books', methods=["GET"])
def get_all_books():
    books = api_functions.get_books()
    return jsonify(books)

@app.route('/books/v1/add', methods=["POST"])
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
    build_table()
    """
    Here you can change debug and port
    Remember that, in order to make this API functional, you must set debug in False
    """
    app.run(host='127.0.0.1', port=8000, debug=False)