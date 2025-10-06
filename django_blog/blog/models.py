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
    
class Comment(models.Model):
    """
    Comment left by a user on a Post.
    - post: which Post this comment belongs to
    - author: the user who wrote the comment
    - content: the body of the comment
    - created_at: when the comment was created
    - updated_at: when the comment was last updated
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"