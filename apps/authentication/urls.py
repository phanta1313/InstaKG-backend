from django.urls import path
from .views import RegisterAPIView, LoginAPIView, UserInfoAPIView

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('info/', UserInfoAPIView.as_view())
]