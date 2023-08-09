from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.documentation import include_docs_urls

app_name = "root"

urlpatterns = [
    path("", include("newspaper.urls")),
    path("user/", include("users.urls")),
    path("admin/", admin.site.urls),
    path("docs/", include_docs_urls(title="NewspaperAPI", public=True), name="docs-page"),
    # path('api-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # included in user logging in function view
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
