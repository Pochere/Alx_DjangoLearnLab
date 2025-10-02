from django.db import models
from django.conf import settings
from django.contrib.auth.models import User 

# Create your models here.
# Using the active user model
User = settings.AUTH_USER_MODEL if isinstance(settings.AUTH_USER_MODEL, str) else settings.AUTH_USER_MODEL

class Post(models.Model):
    """
    Blog Post model for the django_blog project.
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts'
    )

    def __str__(self):
        return self.title
