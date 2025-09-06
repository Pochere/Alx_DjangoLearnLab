
from bookshelf.models import Book

# Update the book title
book = Book.objects.get(title="1984")
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output:
# Title updated successfully to "Nineteen Eighty-Four"
