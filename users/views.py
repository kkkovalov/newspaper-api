from django.http import JsonResponse, HttpResponse
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import user_passes_test

# rest_framework packages
from rest_framework import serializers
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions as rest_exceptions
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# local packages
from users.serializers import UserSerializer


# verifying the user's email in the database
@api_view(["POST"])
def verifyUserExists(request):
    email = request.data["email"]
    try:
        user = get_user_model().objects.get(email=email)
    except:
        return Response(
            {
                "detail": "User does not exist",
                "user_found": False,
            },
            status=404,
        )
    if user is not None:
        return Response(
            {"detail": "User exists in the database", "user_found": True}, status=200
        )
    else:
        # response guard for any issues
        return Response(
            {"detail": "Something went wroung, please try again."}, status=404
        )


# logging in the user
@api_view(["POST"])
def loginUser(request):
    if request.user.is_authenticated:
        return Response({"detail": "Logged in already", "logged_in": True}, status=200)

    email = request.data["email"]
    password = request.data["password"]

    try:
        user = get_user_model().objects.get(email=email)
    except:
        raise rest_exceptions.AuthenticationFailed("User not found")
    if user is not None:
        if not user.check_password(password):
            raise rest_exceptions.AuthenticationFailed("Incorrect password")

        user.update_last_login()
        refresh = RefreshToken.for_user(user)
        return Response(
            {
                "detail": "User found",
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
    else:
        return Response({"detail": "User not Found"}, status=404)


class RegisterUser(APIView):
    def post(self, request, format=None):
        if request.user.is_authenticated:
            return Response({"logged_in": True}, status=200)
        # created a user based on user info (email, password)
        user = UserSerializer(data=request.data)
        user.is_valid(raise_exception=True)
        user.save()
        return Response({"detail": "Successfully added the user"}, status=200)


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def updateUser(request):
    serializer = UserSerializer(request.user, data=request.data, partial=True)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response(serializer.data)


# @api_view(["POST"])
# @permission_classes([IsAuthenticated])
# @user_passes_test(is_creator, login_url='bad-request')
# def testAPI(request):
#     serializer = UserSerializer(request.user, data=request.data, partial=True)
#     serializer.is_valid(raise_exception=True)
#     serializer.save()
#     return Response(serializer.data)
