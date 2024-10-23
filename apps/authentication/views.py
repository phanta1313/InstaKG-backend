from rest_framework import generics
from .serializers import RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from .models import CustomUser
from .services import LoginService


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        CustomUser.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )

        return Response({"status": "User created!"})
    

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    service = LoginService()

    def post(self, request, *args, **kwargs):
        user = self.service.find_user(request)
        self.service.check_user(request, user)
        access, refresh = self.service.give_token(user)
        return Response({'access_token': str(access), 'refresh_token': str(refresh)})
    

class UserInfoAPIView(generics.ListAPIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        return Response({'username': str(user)})
