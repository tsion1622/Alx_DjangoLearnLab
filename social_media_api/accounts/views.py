from rest_framework import generics, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model
from .serializers import UserRegistrationSerializer

User = get_user_model()

# Register
class RegisterView(generics.CreateAPIView):
    serializer_class = UserRegistrationSerializer

# Login
class LoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data["token"])
        return Response({
            "token": token.key,
            "user_id": token.user_id,
            "username": token.user.username
        })

# Profile
class ProfileView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email,
        })
