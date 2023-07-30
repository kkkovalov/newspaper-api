from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.documentation import include_docs_urls

app_name = "root"

urlpatterns = [
    path('', include('newspaper.urls')),
    path('admin/', admin.site.urls),
    path('api-refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('docs/', include_docs_urls(title="NewspaperAPI", public=True), name='docs-page'),
    # included in user logging in function view
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
]
