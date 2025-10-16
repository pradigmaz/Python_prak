from django.shortcuts import render
from .models import Post

def blog_view(request):
    posts = Post.objects.order_by('-date')
    return render(request, 'blog/blog.html', {"posts": posts, "posts_count": posts.count()})
