from django.urls import path
from .views import PostListAPIView, PostCreateAPIView, PostDeleteAPIView


urlpatterns = [
    path('post/list/', PostListAPIView.as_view()),
    path('post/create/', PostCreateAPIView.as_view()),
    path('post/delete/', PostDeleteAPIView.as_view())

]