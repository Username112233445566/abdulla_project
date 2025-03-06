from django.urls import path
from .views import (
    RegisterView, CustomTokenObtainPairView, UserProfileView,
    register_template, login_template, profile_template
)

urlpatterns = [
    path('api/register/', RegisterView.as_view(), name='api-register'),
    path('api/login/', CustomTokenObtainPairView.as_view(), name='api-login'),
    path('api/profile/', UserProfileView.as_view(), name='api-profile'),
    
    path('register/', register_template, name='register'),
    path('login/', login_template, name='login'),
    path('profile/', profile_template, name='profile'),
    path('', login_template, name='login'),
]
