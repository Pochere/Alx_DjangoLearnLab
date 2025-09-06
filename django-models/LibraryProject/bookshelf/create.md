from bookshelf.models import Book

# Create a Book instance
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

# Expected Output:
# Book instance created successfully with id=1 (or next available id)
