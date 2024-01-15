from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')
        extra_kwargs = {'password': {'write_only': True}} # Hides the password before sending back to client, for security reasons

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
