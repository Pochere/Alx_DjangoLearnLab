```python
from bookshelf.models import Book

# ------------------- CREATE -------------------
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
# Expected Output:
# <Book: 1984 by George Orwell (1949)>

# ------------------- RETRIEVE -------------------
book = Book.objects.get(title="1984")
book.title, book.author, book.publication_year
# Expected Output:
# ('1984', 'George Orwell', 1949)

# ------------------- UPDATE -------------------
book.title = "Nineteen Eighty-Four"
book.save()
book.title
# Expected Output:
# 'Nineteen Eighty-Four'

# ------------------- DELETE -------------------
book.delete()
# Expected Output:
# (1, {'bookshelf.Book': 1})

Book.objects.all()
# Expected Output:
# <QuerySet []>
