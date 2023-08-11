from users.views import (
    CustomTokenObtainPairView,
    CustomTokenVerifyView,
    CustomTokenRefreshView,
    LogoutView
)
from django.urls import path, include

urlpatterns = [
    path('jwt/create/', CustomTokenObtainPairView.as_view()),
    path('jwt/refresh/', CustomTokenRefreshView.as_view()),
    path('jwt/verify/', CustomTokenVerifyView.as_view()),
    path('logout/', LogoutView.as_view()),
]
