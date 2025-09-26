from django.db import models

# Creating my models below.
# The Author model represents a book author in our system.
# Each Author can be linked to multiple Books (One-to-Many relationship)

class Author(models.Model):
    name = models.CharField(max_length=100) #stores the name of the Author

    def __str__(self):
        return self.name # makes admin/shell outputs more readable

# The Book model represents a single book.
# Each Book is linked to exactly one Author via a ForeignKey.

class Book(models.Model):
    title = models.CharField(max_length=200) #stores the book title
    publication_year = models.PositiveIntegerField(null=True, blank=True) # stores the year of the book
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return self.title
