from flask import Flask, jsonify, request
#The request object from flask is imported in order to handle incoming HTTP requests. 

app = Flask(__name__)

# Sample data for books
books = [
    {"id": 1, "title": "Python Programming", "author": "John Doe"},
    {"id": 2, "title": "Flask Essentials", "author": "Jane Doe"},
    {"id": 3, "title": "Python for Data Science", "author": "Aryana"},
    {"id": 4, "title": "Web Development with Flask", "author": "Blake Lively"}
]
# sample data for members
members = [

    {'id': 1, 'name': 'John Doe', 'email': 'john.doe@abc.com'},
    {'id': 2, 'name': 'Jane Smith', 'email': 'jane.smith@abc.com'},
    {'id': 3, 'name': 'Aryana', 'email': 'Aryana@abc.com'},
    {'id': 4, 'name': 'Blake Lively', 'email': 'blake.lively@abc.com'}
]

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the Library Management System API",
        "routes": [
            {"method": "GET", "endpoint": "/books", "description": "List all books"},
            {"method": "POST", "endpoint": "/books", "description": "Add a new book"},
            {"method": "GET", "endpoint": "/members", "description": "List all members"}
        ]
    })

@app.route('/favicon.ico')
def favicon():
    return '', 204  # No content response






# Finding item using its ID, this function is used in crud operations below:-
def find_by_id(datalist, item_id):
    "** Search for an item in the list using its ID. **"
    for item in datalist:
        if item['id'] == item_id:
            return item
    return None


# CRUD operation for books :
@app.route('/books', methods=['GET'])  # Retrieve books
def get_books():
    """
    Fetch all books or search by title/author using query parameters.
    - If 'title' or 'author' query parameters are provided, filters the books.
    - Returns all books if no query parameters are given.
    """
    title = request.args.get('title', '').lower()
    author = request.args.get('author', '').lower()

    # If search parameters are provided, filter the books based on title or author
    if title or author:
        filtered_books = [
            book for book in books
            if (title in book['title'].lower() if title else True) and
               (author in book['author'].lower() if author else True)
        ]
        return jsonify(filtered_books)

    # Return all books if no search parameters
    return jsonify(books)


@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    "Fetch book by its ID."
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    return jsonify(book)


@app.route('/books', methods=['POST'])          #Adding new item 
def add_book():
    "Add new book."
    data = request.json
    if not data or not all(key in data for key in ('title', 'author', 'year')):
        return jsonify({'message': 'Invalid input. Title, author, and year are required.'}), 400

    if not isinstance(data['year'], int):
        return jsonify({'message': 'Year must be an integer.'}), 400

    # Creating the new book
    new_book = {
        'id': len(books) + 1,
        'title': data['title'],
        'author': data['author'],
        'year': data['year']
    }
    books.append(new_book)
    return jsonify(new_book), 201


@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """
    Update an existing book by its ID.
    """
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    data = request.json
    if not data:
        return jsonify({'message': 'No data provided for update.'}), 400

    # Update book details with the provided data
    book['title'] = data.get('title', book['title'])
    book['author'] = data.get('author', book['author'])
    book['year'] = data.get('year', book['year'])
    return jsonify(book)


@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """
    Delete a book by its ID.
    """
    book = find_by_id(books, book_id)
    if not book:
        return jsonify({'message': 'Book not found'}), 404

    books.remove(book)
    return jsonify({'message': f'Book with ID {book_id} has been deleted.'})


# Members CRUD
@app.route('/members', methods=['GET'])
def get_members():
    "Fetch all members."
    return jsonify(members)


@app.route('/members/<int:member_id>', methods=['GET'])
def get_member(member_id):
    "Fetch single member by their ID."
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404

    return jsonify(member)


@app.route('/members', methods=['POST'])
def add_member():
    """
    Add a new member.
    """
    data = request.json
    if not data or not all(key in data for key in ('name', 'email')):
        return jsonify({'message': 'Invalid input. Name and email are required.'}), 400

    # Creating the new member
    new_member = {
        'id': len(members) + 1,
        'name': data['name'],
        'email': data['email']
    }
    members.append(new_member)
    return jsonify(new_member), 201


@app.route('/members/<int:member_id>', methods=['PUT'])
def update_member(member_id):
    "Update an existing member by their ID."
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404

    data = request.json
    if not data:
        return jsonify({'message': 'No data provided for update.'}), 400

    # Update member details with the provided data
    member['name'] = data.get('name', member['name'])
    member['email'] = data.get('email', member['email'])
    return jsonify(member)


@app.route('/members/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    "Delete a member by their ID."
    member = find_by_id(members, member_id)
    if not member:
        return jsonify({'message': 'Member not found'}), 404

    members.remove(member)
    return jsonify({'message': f'Member with ID {member_id} has been deleted.'})


if __name__ == '__main__':
    app.run(debug=True)