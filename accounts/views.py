from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import CustomUserSerializer
from django.contrib.auth.models import User

@api_view(['POST'])
def signup_view(request):
    if request.method == 'POST':
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # creates a new user
            return Response({
                'response': "Successfully registered a new user.",
                'username': serializer.data.get('username')
            })
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login_view(request):
    # Gets username and password from the request data
    username = request.data.get('username')
    password = request.data.get('password')

    print("Username:", username)
    print("Password:", password)

    user = authenticate(request, username=username, password=password)
    print("User authenticated:", user is not None)

    
    if user is not None: # If authentication successful, log user in 
        login(request, user)
        print("User logged in:", request.user.is_authenticated)
        return Response({'response': 'Successfully logged in.'})
    else:
        print("Login failed")
        return Response({'response': 'Invalid credentials.'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_view(request):
    logout(request)
    return Response({'response': 'Successfully logged out.'})

