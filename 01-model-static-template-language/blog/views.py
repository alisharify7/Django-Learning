# Create your views here.
from django.views.generic import ListView
from .models import Post

class BlogListView(ListView):
    template_name = "blog/home.html"
    model = Post
    context_object_name = "blog"