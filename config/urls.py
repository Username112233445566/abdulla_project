from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from apps.user.views import (
    RegisterView, CustomTokenObtainPairView, UserProfileView,
    register_template, auth_template, profile_template
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/auth/', csrf_exempt(CustomTokenObtainPairView.as_view()), name='api-login'),
    path('api/profile/', UserProfileView.as_view(), name='api-profile'),
    
    path('register/', register_template, name='register'),
    path('auth/', auth_template, name='auth'),
    path('profile/', profile_template, name='profile'),
    path('', auth_template, name='auth'),
]
