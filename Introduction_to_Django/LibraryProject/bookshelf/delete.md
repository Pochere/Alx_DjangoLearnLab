# Delete the book
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Expected Output:
# (1, {'bookshelf.Book': 1})   # 1 record deleted

# Confirm deletion
Book.objects.all()

# Expected Output:
# <QuerySet []>
