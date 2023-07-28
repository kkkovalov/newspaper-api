from django.http import JsonResponse, HttpResponse
from django.core import exceptions
from django.contrib.auth import authenticate
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
        user = models.User.objects.get(email=email)
    except:
        return Response({'detail': 'User does not exist', 'user_found': False,}, status=404)
    if user is not None:
        return Response({'detail': 'User exists in the database', 'user_found': True}, status=200)

# logging in the user
@api_view(["POST"])
def loginUser(request):
    if request.user.is_authenticated:
        return Response({'detail': 'Logged in already', 'logged_in': True}, status=200)
    
    elif request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = models.User.objects.get(email=email)
        except:
            raise rest_exceptions.AuthenticationFailed()
        user = authenticate(request, email=email, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            login(request,user)
            return JsonResponse({
                'message': 'user found',
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                })
        else:
            return JsonResponse({'message': 'user not found', }, status=404)
    else:
        return Response({'detail': 'Something went wrong, please try again.'}, status=404)

@api_view(['POST'])
def registerUser(request):
    if request.method == 'POST':
        
        if request.user.is_authenticated():
            return JsonResponse({'logged_in': True})
        
        # created a user based on user info (username, email, password1, password2)
        user = forms.ReaderCreationForm(request.POST)
        # if request.POST.get('email') == '':
        #     raise rest_exceptions.ValidationError
        if user.is_valid():
        
            user.save()
            return JsonResponse({'message': 'Successfuly added a user'})
        else:
            raise rest_exceptions.ValidationError
    else:
        raise rest_exceptions.APIException