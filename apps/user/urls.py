from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from apps.user.views import (
    RegisterView, CustomTokenObtainPairView, UserProfileView,
    register_template, auth_template, profile_template
)
from .views import auth_template

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/auth/', csrf_exempt(CustomTokenObtainPairView.as_view()), name='api-auth'),
    path('api/profile/', UserProfileView.as_view(), name='api-profile'),
     path('auth/', auth_template, name='auth'),
    path('register/', register_template, name='register'),
    path('profile/', profile_template, name='profile'),
    path('', auth_template, name='auth'),
]
