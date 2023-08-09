from django.urls import path
from users.views import (
    verifyUserExists,
    loginUser,
    updateUser,
    RegisterUser,
)

urlpatterns = [
    path("verify/", verifyUserExists, name="user-verify"),
    path("login/", loginUser, name="user-login"),
    path("register/", RegisterUser.as_view(), name="user-register"),
    path("update/", updateUser, name="user-update"),
]
