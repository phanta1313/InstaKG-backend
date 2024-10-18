from django.shortcuts import redirect
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment
from .serializers import PostListSerializer, PostCreateDeleteSerializer


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostListSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateDeleteSerializer
    permission_classes = (IsAuthenticated,)


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostCreateDeleteSerializer
    permission_classes = (IsAuthenticated,)
