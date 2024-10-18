from rest_framework import serializers
from .models import Post


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("image", "text", "likes")


class PostCreateDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("image", "text")