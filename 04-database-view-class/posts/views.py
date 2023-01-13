from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello world! ")


from .models import Post
def show_posts(request):
    posts= Post.objects.all()
    print(posts)
    context = {
        "post": posts,
    }
    return render(request,"index.html", context=context)