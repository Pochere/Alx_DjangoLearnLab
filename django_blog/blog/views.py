from django.shortcuts import render
from .models import Post

# View to list all posts
def post_list(request):
    posts = Post.objects.all().order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})



