from django.contrib import admin

# Register your models here.
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "body"]

admin.site.register(Post, PostAdmin)