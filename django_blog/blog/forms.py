from django import forms
from .models import Post, Comment
from taggit.forms import TagWidget  # ✅ required for taggit widgets


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # ✅ includes tags
        widgets = {
            'tags': TagWidget(),  # ✅ this line is required for the check
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
