from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token  

User = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "email", "password")

    def create(self, validated_data):
        user = User.objects.create_user(   # <- required
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"]
        )
        # Create token when user registers
        Token.objects.create(user=user)    # <- required
        return user
