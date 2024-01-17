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
        data = {}
        if serializer.is_valid():
            user = serializer.save() # creates a new user by calling the overridden create method in serializers.py 
            data['response'] = "Successfully registered a new user."
            data['username'] = user.username
        else:
            data = serializer.errors # captures any errors and includes in response
        return Response(data)

@api_view(['POST'])
def login_view(request):
    print("login_view is called")
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None: # if user exists in database (authenticated)
        login(request, user)
        return Response(status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
