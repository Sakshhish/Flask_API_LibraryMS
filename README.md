# Flask_API_LibraryMS
Hey, welcome to my repo, this is a basic library management code using flask webframework, in this we are using lists in order to avoid a database linking.
The code is run and tested using thunderclient.
Let me take you through the project:

## How to Run the Project
### Prerequisites:
Make sure you have the following installed:
- Python 3.x
- Flask (Python web framework)
### Steps to Run:
1. Clone the repository:
   bash
   git clone <repository-link>
   cd <repository-name>
### Make sure you have flask installed, if not, run:
- pip install flask

### Run the application:
- python app.py

## Testing:
#### Using Thunderclient
//Searching books by title, authorname:
GET: http://127.0.0.1.5000/books
GET: http://127.0.0.1:5000/books?title=python
GET: http://127.0.0.1:5000/books?author=Aryana
GET http://127.0.0.1:5000/books?title=python&author=Aryana

//Add new book
POST http://127.0.0.1:5000/books
(add new book data in data section)
{
  "id": 11,
  "title": "Learning Python",
  "author": "Alex Smith"
}

//Update existing books data:
PUT: http://127.0.0.1:5000/books/1

ADD SOME DATA TO BE UPDATED:
{
  "message": "Book updated successfully!",
  "book": {
    "id": 1,
    "title": "Python Programming - Updated",
    "author": "John Doe Updated"
  }
}

// Delete a book
DELETE: http://127.0.0.1:5000/books/1
----- here, 1 is id ------




## Design Choices

- **In-memory storage**: 
  To simplify the implementation, books and members data are stored in Python lists (`books` and `members`) instead of using a database. This avoids the need for a database setup and allows focusing on core functionality.

- **RESTful API**:
  The API follows REST conventions with CRUD (Create, Read, Update, Delete) operations for managing books and members.

- **Pagination**:
  Pagination is implemented to limit the number of results returned per request. It allows users to request specific pages and control the number of items per page using `page` and `per_page` query parameters.

- **Search functionality**:
  The API supports searching books by `title` and `author` using query parameters. This makes it easier to filter books based on these fields.

- **Testing**:
  The API can be tested using ThunderClient (or any HTTP client). Example requests and responses are provided to help users test the API endpoints.
