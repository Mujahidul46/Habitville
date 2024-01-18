from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from django.http import HttpResponse

@api_view(['POST'])
def signup_view(request):
    print("Signup_view is called")
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # creates a new user
            return Response({
                'response': "Successfully registered a new user.",
                'username': user.username
            })
        else:
            # Check if the username already exists
            if 'username' in serializer.errors:
                return Response({
                    'username_exists': True, # flag to let frontend know if username exists
                    'message': "A user with that username already exists."
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# no longer need Login_view function as TokenObtainPairView in urls.py handles user authentication and token generation