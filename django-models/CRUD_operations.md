```python
# Create
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984 by George Orwell (1949)

# Retrieve
books = Book.objects.all()
for book in books:
    print(book.title, book.author, book.publication_year)
# Output:
# 1984 George Orwell 1949

# Update
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()
print(book.title)
# Output: Nineteen Eighty-Four

# Delete
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

books = Book.objects.all()
print(books)
# Output: <QuerySet []>
