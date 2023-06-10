from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample data
books = [
    {"id": 1, "title": "Book 1", "author": "Author 1"},
    {"id": 2, "title": "Book 2", "author": "Author 2"},
    {"id": 3, "title": "Book 3", "author": "Author 3"}
]

# GET /books?author=AuthorName&category=CategoryName
@app.route('/books', methods=['GET'])
def get_books():
    author = request.args.get('author')
    category = request.args.get('category')
    
    print(author)
    print(category)

    # Logic to filter books based on author and category
    
    return jsonify({"author": author})

# POST /books - Create a new book
@app.route('/books', methods=['POST'])
def create_book():
    new_book = {
        'id': len(books) + 1,
        'title': request.json['title'],
        'author': request.json['author']
    }
    books.append(new_book)
    return jsonify(new_book), 201

# PUT /books/:id - Update a book
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((b for b in books if b['id'] == book_id), None)
    if book:
        book['title'] = request.json['title']
        book['author'] = request.json['author']
        return jsonify(book)
    else:
        return jsonify({'error': 'Book not found'}), 404

# DELETE /books/:id - Delete a book
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [b for b in books if b['id'] != book_id]
    return jsonify({'message': 'Book deleted'})

# Run the API server
if __name__ == '__main__':
    app.run()