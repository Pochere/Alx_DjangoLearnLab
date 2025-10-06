from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment, Tag


class PostForm(forms.ModelForm):
    """
    Form for creating and editing blog posts, including tags.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # include tags in the form


class CommentForm(forms.ModelForm):
    """
    Form for creating and editing comments on posts.
    """
    class Meta:
        model = Comment
        fields = ['content']
