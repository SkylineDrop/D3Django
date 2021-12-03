from django.views.generic import ListView, DetailView

from .models import Post

class PostList(ListView):
    model = Post
    template_name = 'news.html' 
    context_object_name = 'news'

class PostDetail(DetailView):
    model = Post
    template_name = 'definite_news.html' 
    context_object_name = 'definite_news'