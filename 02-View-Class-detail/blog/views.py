# Create your views here.
from django.views.generic import ListView, DetailView
from .models import Post

class BlogListView(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "blog"


class BlogDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"