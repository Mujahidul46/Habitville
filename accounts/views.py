from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CustomUserSerializer
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def signup_view(request):
    print("Signup_view is called")
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # creates a new user
            
            # Generate a token for the new user
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            
            return Response({
                'response': "Successfully registered a new user.",
                'username': user.username,
                'token': token  # Return the JWT to the frontend
            })
        else:
            if 'username' in serializer.errors:
                return Response({
                    'username_exists': True,
                    'message': "A user with that username already exists."
                }, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# no longer need Login_view function as TokenObtainPairView in urls.py handles user authentication and token generation