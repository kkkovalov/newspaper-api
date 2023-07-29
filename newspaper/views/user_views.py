from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm

# rest_framework packages
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions
from rest_framework_simplejwt.tokens import RefreshToken

# local packages
from newspaper import models, forms
from newspaper.serializers import ArticleSerializer, UserSerializer

# verifying the user's email in the database
@api_view(['POST'])
def verifyUserExists(request):
    email = request.POST.get('email')
    try:
        user = get_user_model().objects.get(email=email)
    except:
        return Response({'detail': 'User does not exist', 'user_found': False,}, status=404)
    if user is not None:
        return Response({'detail': 'User exists in the database', 'user_found': True}, status=200)

# @api_view(["POST"])
# def testAPI(request):
#     serializer = UserSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)
    

# logging in the user
@api_view(["POST"])
def loginUser(request):
    if request.user.is_authenticated:
        return Response({'detail': 'Logged in already', 'logged_in': True}, status=200)
    
    email = request.POST.get('email')
    password = request.POST.get('password')
    
    try:
        user = get_user_model().objects.get(email=email)
    except:
        raise rest_exceptions.AuthenticationFailed('User not found')
    if user is not None:
        if not user.check_password(password):
            raise rest_exceptions.AuthenticationFailed('Incorrect password')
        
        user.update_last_login()
        refresh = RefreshToken.for_user(user)
        return Response({
            'detail': 'User found',
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            })
    else:
        return JsonResponse({'message': 'User not Found', }, status=404)


# registering new user
@api_view(['POST'])
def registerUser(request):
        
    if request.user.is_authenticated:
        return JsonResponse({'logged_in': True})
        
    # created a user based on user info (email, password)
    user = UserSerializer(data=request.data)
    user.is_valid(raise_exception=True)
    user.save()
    return Response({'detail': 'Successfully added the user'}, status=200)