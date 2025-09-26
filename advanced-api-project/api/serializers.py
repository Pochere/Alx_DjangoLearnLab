from rest_framework import serializers
from .models import Book, Author
import datetime

# Serializer for the Book model
# Converts Book objects ↔ JSON
# Also includes validation for publication_year to prevent future dates

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
# Custom validation: publication_year cannot be in the future
    def validate_publication_year(self, value):
        if value is None:
            return value
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("publication_year cannot be in the future.")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    # Nested representation of books related to this author
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['id', 'name', 'books']
