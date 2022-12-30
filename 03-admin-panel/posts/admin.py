from django.contrib import admin

# Register your models here.

from .models import Post, Comment




class Commentadmininline(admin.TabularInline):
    model = Comment
    fields = ("text", "enable")
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = ("id","text", "title", "Created_At")
    inlines = (Commentadmininline,)

admin.site.register(Post,PostAdmin)

