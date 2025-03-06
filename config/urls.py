from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.user.urls')),
    path('api/lessons/', include('apps.lessons.urls')),
    path('', include('apps.user.urls')),
]
