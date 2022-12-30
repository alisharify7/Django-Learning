from django.db import models

# Create your models here.



class Post(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    enable = models.BooleanField(default=False)
    Created_At = models.DateField(auto_now_add=True)
    Update_At = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title[:25]


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    text = models.TextField(null=True, blank=True)
    enable = models.BooleanField(default=False)
    Created_At = models.DateField(auto_now_add=True)
    Update_At = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.text[:25]