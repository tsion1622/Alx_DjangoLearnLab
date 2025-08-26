from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = Book.objects.filter(author=author)

# List all books in a library
library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()

# Retrieve the librarian for a library
librarian = Librarian.objects.get(library=library)

print("Books by author:", [book.title for book in books_by_author])
print("Books in library:", [book.title for book in books_in_library])
print("Librarian name:", librarian.name)
