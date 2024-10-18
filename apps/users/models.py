from django.db import models
from apps.authentication.models import CustomUser


class Post(models.Model):
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to="posts/")
    likes = models.IntegerField(default=0)

    def on_create(self, request):
        self.owner = request.user


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
