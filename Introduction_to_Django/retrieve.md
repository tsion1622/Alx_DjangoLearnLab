```python
from bookshelf.models import Book

# Retrieve all books
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949

# Retrieve a single book using get()
book = Book.objects.get(title="1984")
print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949
