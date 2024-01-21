from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'username', 'password', 'goals')  
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Update the CustomUser instance
        instance.username = validated_data.get('username', instance.username)
        instance.goals = validated_data.get('goals', instance.goals)
        instance.set_password(validated_data.get('password', instance.password))
        instance.save()
        return instance
