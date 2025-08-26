## API Endpoints

- `GET /api/books/` → List all books
- `GET /api/books/<id>/` → Retrieve a book
- `POST /api/books/create/` → Create a book (auth required)
- `PUT /api/books/<id>/update/` → Update a book (auth required)
- `DELETE /api/books/<id>/delete/` → Delete a book (auth required)

Permissions:
- List & Detail → Public access
- Create, Update, Delete → Authenticated users only

### Filtering, Searching, and Ordering

- Filter by field:
  - `/api/books/?title=Harry Potter`
  - `/api/books/?publication_year=1997`
- Search across title and author name:
  - `/api/books/?search=Rowling`
- Order results:
  - `/api/books/?ordering=title`
  - `/api/books/?ordering=-publication_year`
